# This is a script someone external wrote and you want to also use it.
# It has a requirements.txt so you can use that to install the packages needed
# First create and then activate your virutal environment
# Then install what's in requirements.txt viathe command
# pip install -r requirements.txt

import requests
from bs4 import BeautifulSoup


r = requests.get('http://www.example.com')
soup = BeautifulSoup(r.text, features="html.parser")
print(soup.text)
