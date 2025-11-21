# 1. Use the  beautifulsoup4  module to extract the following information and store it in variables:

# The title of the page (<title> );

# The text of the <h1> tag;

# The names and prices of the products in the list (<ul> ) (store them in a list);

# The descriptions of the products in the list (<ul> ) (store them in a list).

# 2. Display the extracted information in the console.

# 3. Convert the prices to dollars (consider that  dollar = euro * 1.2  ).

# 4. Display the new list with the name and the new price in dollars.

# Once you have completed the exercise, you can run the following command in the VS code terminal  pytest tests.py

import requests
from bs4 import BeautifulSoup4

# import html from index.html

page = 

# 'open' gets a file and returns it as a file object
# 'with' helps ensure the file is properly closed when the block is exited (in leiu for something like file.close()) 
# 'r' indicates opening the file for reading
# 'encoding' is for the type of encoding (HTML uses UTF-8)
with open("index.html", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# This will get the whole tag, i.e. <title>HTML Extraction Exercises</title>
title = soup.title

h1_text = soup.h1.string

print(title)
print(h1_text)