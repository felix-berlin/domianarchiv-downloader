import requests
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse, unquote
import argparse
import os

base_url = "https://domianarchiv.de"

# Create the parser
parser = argparse.ArgumentParser(description="Download mp3 files")

# Add the arguments
parser.add_argument('--start_page', type=int, default=0, help='The start page number')
parser.add_argument('--end_page', type=int, default=184, help='The end page number')
parser.add_argument('--download_dir', type=str, default="downloads", help='The directory to download the files to')

# Parse the arguments
args = parser.parse_args()

start_page = args.start_page
end_page = args.end_page
download_dir = args.download_dir

for page_number in range(start_page, end_page + 1):
    # Handle the first page as a special case
    if page_number == 0:
        search_url = f"{base_url}/sendungen"
    else:
        # Append the page number to the URL as a query parameter
        search_url = f"{base_url}/sendungen?page={page_number}"

    r = requests.get(search_url)

    soup = BeautifulSoup(r.text, 'html.parser')

    links = soup.find_all('a')

    # Filter for links that lead to the download page
    download_page_links = [link['href'] for link in links if link['href'].endswith('.m4a')]
    # print(f"{download_page_links}")
    for page_link in download_page_links:
        print(f"{page_link}")
        page_link = page_link.replace('https://domianarchiv.de/', 'https://domian-download.de/HanseMerkur/')
        # Follow the link to the download page
        r = requests.get(f"{page_link}")
        soup = BeautifulSoup(r.text, 'html.parser')

        # Find the actual download link on the new page
        # This depends on the structure of the page, you might need to adjust this
        # Find all links on the page
        all_links = soup.find_all('a')

        # Select the last link
        download_link = all_links[-1]['href'] if all_links else None


        path = urlparse(unquote(download_link)).path
        filename = path.split("/")[-1]

        # When downloading the file, use the download directory
        try:
            filepath = os.path.join(download_dir, filename)
            urllib.request.urlretrieve(download_link, filepath)
            print(f"Downloaded {filename} to {download_dir}")  # print a message for each file downloaded
        except Exception as e:
            print(f"Failed to download {download_link} to {download_dir}: {e}")  # print a message if a download fails