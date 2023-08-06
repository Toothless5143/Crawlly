# Crawlly
Crawlly is a basic python crawler to scrape different endpoints from a provided URL. It uses the `requests` library to send a GET request to a specified URL and the `BeautifulSoup` library to parse the HTML content of the response. The script then finds all the anchor `<a>` tags in the page and prints the URLs of the links present on that page.

### Installation
First you need to clone the repo and you need to install some pip libraries. You can do it by following the below command. <br>
```shell
git clone https://github.com/Toothless5143/Crawlly.git && cd crawlly
pip install -r requirements.txt
```

Then you need to fire up the tool.<br>
```shell
python3 crawlly.py
```

### License
This tool is open source and available under the [MIT License.](/LICENSE)
