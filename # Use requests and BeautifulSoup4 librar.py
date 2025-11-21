# Use requests and BeautifulSoup4 libraries to get article descriptions from the UK government news site. 

import requests
from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page,'html.parses')

# Inspecting article descriptions show they are <p> elements with the class name gem-c-document-list__item-description
descriptions = soup.find_all('p', class_='gem-c-document-list__item-description')

for description in descriptions
    print(description.string)
    