# Loop through all the pages in http://quotes.toscrape.com/ and get all the unique authors on the website.
# Unknown Number of Pages, but knowledge of last page

import requests
import bs4

# Step 1: Find the error sentence for a page that we know doesn't exist (e.g. http://quotes.toscrape.com/page/999999)
url = 'http://quotes.toscrape.com/page/'

# choose some huge page number we know doesn't exist
page_url = url + str(99999999)

# obtain request
res = requests.get(page_url)

# Turn into soup
soup = bs4.BeautifulSoup(res.text, 'lxml')

# Check if error sentence exist
'No quotes found!' in res.text

# Step 2: List the authors
page_still_valid = True
authors = set()
page = 1

while page_still_valid:

    # Concatenate to get new page URL
    page_url = url + str(page)

    # Obtain request
    res = requests.get(page_url)

    # check to see if we are on the last page
    if "No quotes found!" in res.text:
        break

    # turn into soup
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # Add authors to our set
    for name in soup.select(".author"):
        authors.add(name.text)

    # Go to next page
    page += page

print(authors)

