# pull_data.py
# Elinor Frost

# This file can be used to extract post information from a webpage. The data is sent to a json file.

# Starter code from codecademy's https://www.youtube.com/watch?v=b8q98xvyIqg
import requests
import bs4
import json

# TODO: formatting, creating main(), standardizing, etc

# TODO: add input call to get url from user

url = "https://healthunlocked.com/share-metastatic-support/posts/152472194/enhertu"
# url = "https://healthunlocked.com/share-metastatic-support/posts/152461923/tips-on-tamoxifen-and-ibrance"

def extract_source(url):
    """From a given url, return the html in text.
    Adapted from https://stackoverflow.com/questions/41982475/scraper-in-python-gives-access-denied

    Parameters: url (str) - the url of the web page

    Returns: source (str) - a string representation of the html
    """
    agent = {"User-Agent":"Mozilla/5.0"}
    source=requests.get(url, headers=agent).text
    return source

def find_content(url, selector='#__next > div > main > div.sc-64ce13e7-0.bgfGvQ > div.sc-64ce13e7-1.fDANYB > div > section:nth-child(2) > div.sc-7c31747b-1.gbAPbK.js-post-body p'):
    """From a given url and a css selector, returns the content

    Parameters: url (str) - the url of the web page
                selector (str) - the CSS selector to use for the webpage.

    Returns: post_content (str) - a string representation of the content requested
    """
    soup = bs4.BeautifulSoup(extract_source(url), "html.parser")
    content = soup.select(selector)
    return content

# format post id and title from url
post_name = url.split("/")[-2:]
post_id = post_name[0]
post_title = str(post_name[-1])

# extract content into a dictionary
post = {}
post["id"] = post_id
post["title"] = post_title
post["content"] = str(find_content(url).pop()).strip("<p>")

#TODO: extract metadata to add to dictionary, including username and post date

# save to json
# TODO: Decide if we want to return the json object instead of writing directly from this file
with open("post_content.json", "w") as file:
    json.dump(post, file)

