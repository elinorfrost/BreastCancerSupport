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

def find_with_css(soup, selector):
    """From a soup object and a css selector, returns the content

    Parameters: soup (BeautifulSoup) - A soup object of the web page
                selector (str) - the CSS selector to use for the webpage.

    Returns: content (str) - a string representation of the content requested
    """
    content = soup.select(selector)
    return content

def find_with_tag(soup, tag, item):
    """From a soup object, a tag, and the desired item, returns the item's content.
    Parameters: soup (BeautifulSoup) - A soup object of the web page
                tag (str) - the desired tag to locate.
                item (str) - the name of the item within the tag to find and return
    Returns: content (str) - a string representation of the content requested
    """

    tag_ = soup.find(tag)
    content = str(tag_.get(item)) if tag_ else None
    return content

def main(url=url):
    # TODO: consider trying to utilize tags instead of css snippets
    css_selectors = {
        "post_body": '#__next > div > main > div.sc-64ce13e7-0.bgfGvQ > div.sc-64ce13e7-1.fDANYB > div > section:nth-child(2) > div.sc-7c31747b-1.gbAPbK.js-post-body p',
        "post_date": '',
        "username": '#__next > div > main > div.sc-64ce13e7-0.bgfGvQ > div.sc-64ce13e7-1.fDANYB > div > header > div > div:nth-child(1) > a',
        "comments": '#__next > div > main > div.sc-64ce13e7-0.bgfGvQ > div.sc-64ce13e7-1.fDANYB > div > header > div > div:nth-child(2) > a'
    }
    soup = bs4.BeautifulSoup(extract_source(url), "html.parser")

    # format post id and title from url
    post_name = url.split("/")[-2:]
    post_id = post_name[0]
    post_title = str(post_name[-1])

    # extract content into a dictionary
    post = {
        "id": post_id,
        "title": post_title,
        "content": str(find_with_css(soup, css_selectors["post_body"]).pop()).strip("<p>"),
        "date": 'TODO'
        # TODO: collect comment data
        # "comments": {"num_comments": int(str(find_with_css(soup, css_selectors["comments"])).split("/")[-2].strip('nhertu#responses\"> Replies</a>]'))}
    }
    # TODO: Couldn't figure out why .find('button') wasn't working, so I used this terrible string formatting to get the username
    username = str(soup.find(class_="sc-18c93b1d-2 bIGrQn author")).split(">")[-2].split("<")[0]
    post["username"] = username

    print(post)
    return(post)


    # save to json
    # TODO: Decide if we want to return the json object instead of writing directly from this file
    # with open("post_content.json", "w") as file:
    #     json.dump(post, file)

if __name__ == "__main__":
    main()

