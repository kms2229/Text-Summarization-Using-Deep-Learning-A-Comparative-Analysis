import requests
from bs4 import BeautifulSoup

# Make a request to the website
r = requests.get("")

r.content

# Use the 'html.parser' to parse the page
soup = BeautifulSoup(r.content, 'html.parser')

# Find all the `<p>` tags on the page
p_tags = soup.find_all('p')

# Print the text from each `<p>` tag
for tag in p_tags:
    print(tag.text)