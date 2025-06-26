import requests
from bs4 import BeautifulSoup

# URL of the news site
url = "https://inshorts.com/en/read"

# Fetch the page
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all headline divs
headlines = soup.find_all('span', itemprop='headline')

# Save headlines to a .txt file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for headline in headlines:
        text = headline.get_text(strip=True)
        file.write(text + "\n")
        print(text)
