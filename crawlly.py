import requests
from bs4 import BeautifulSoup

def crawl():
    # Ask the user for the URL
    url = input("Enter the URL to crawl: ")
    
    # Send a GET request to the specified URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all the <a> tags in the page
        links = soup.find_all('a')
        
        # Print the URLs of all the links
        for link in links:
            print(link.get('href'))
    else:
        print('Error: Could not fetch the URL.')

# Start crawling by asking for the URL
crawl()
