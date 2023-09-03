# Crawlly: Web Page Crawler

Crawlly is a straightforward Python tool designed for web page crawling and scraping. Using the `requests` library, it sends a GET request to the specified URL and utilizes the `BeautifulSoup` library to parse the HTML content of the response. The script then extracts all anchor `<a>` tags from the page and prints the URLs of the links present.

**Features:**
- Lightweight and efficient web page crawler.
- Scrapes and extracts URLs from a provided web page.
- Utilizes the `requests` library for HTTP requests and `BeautifulSoup` for HTML parsing.

**Installation:**
1. Clone the repository to your local machine using the following command:
   ```shell
   git clone https://github.com/Toothless5143/Crawlly.git && cd crawlly
   ```

2. Install the required dependencies by executing the following command:
   ```shell
   pip install -r requirements.txt
   ```

3. Launch the tool by running the following command:
   ```shell
   python3 crawlly.py
   ```

**License:**
This tool is open source and available under the [MIT License](/LICENSE).
