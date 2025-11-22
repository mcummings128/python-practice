# Use BeautifulSoup with an HTML file to extract, transform and "load" information (load in quotes because we're not really transferring the transformed data anywhere, though you could argue we are to the shell/stdout since we're printing it)

# Instructions

#  1. Use the  beautifulsoup4  module to extract the following information and store it in variables:

# The title of the page (<title> );

# The text of the <h1> tag;

# The names and prices of the products in the list (<ul> ) (store them in a list);

# The descriptions of the products in the list (<ul> ) (store them in a list).

# 2. Display the extracted information in the console.

# 3. Convert the prices to dollars (consider that  dollar = euro * 1.2  ).

# 4. Display the new list with the name and the new price in dollars.

# Once you have completed the exercise, you can run the following command in the VS code terminal  pytest tests.py

from bs4 import BeautifulSoup


def main():
    # import html from index.html by opening it, then reading its contents (like Bash 'cat; command sort of.)

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

    products = soup.find_all("li")
    product_names = []
    product_prices = []
    product_descriptions = []

    for product in products:
        # findChildren is deprecated in Python 3.0.0 but for learning purposes is the easiest to use out of the box. It will get the children of the specified element. recursive=False means only the direct children
        children_tags = product.findChildren(recursive=False)
        product_name = product.find("h2")
        product_names.append(product_name.string)
        # Every price is in format of 'Price : €##' (## being a number). Use split() to delimit and take second piece, then strip trailing whitespace (rstrip()) (Actually rstrip() ended up not being needed but whatever)
        product_price_str = product.find("p").string.split(": €")[1].rstrip()
        # Convert to int and do conversion (this makes product_price become a float)
        product_price = int(product_price_str) * 1.2
        print(f"product price = {product_price}")
        product_prices.append(product_price)
        product_description = children_tags[2]
        print(f"description = {product_description}")
        product_descriptions.append(product_description.string)
        

    print(f"title = {title}")
    print(f"h1_text = {h1_text}")

    print(f"Product information:\n")

    # This range will be 0,1,2
    for i in range(3):
        print(f"- Name: {product_names[i]}")
        # Use :.2f to format float to print to 2 decimal places
        print(f"- Price: ${product_prices[i]:.2f}")
        print(f"- Description: {product_descriptions[i]}")
        print("\n")

if __name__ == "__main__":
    main()