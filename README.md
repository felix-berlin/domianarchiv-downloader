# Domian Archiv Downloader

This script is used to download audio files from the website <https://domianarchiv.de>.

## Requirements

- Python 3
- BeautifulSoup4
- requests

You can install these packages using pip:

```bash
pip install beautifulsoup4 requests
```

## Usage

You can run the script using the following command:

```bash
python domianarchiv-downloader.py --start_page START_PAGE --end_page END_PAGE --download_dir DOWNLOAD_DIR
```

Where:

`START_PAGE` is the page number to start downloading from (default is 0).
`END_PAGE` is the page number to stop downloading at (default is 184).
`DOWNLOAD_DIR` is the directory where the downloaded files will be saved (default is "downloads").

## How it works

The script uses BeautifulSoup to parse the HTML of the website and find the links to the audio files. It then downloads these files using the requests library.

## Disclaimer

Please respect the rights of the content creators and only download the files if you have permission to do so.
