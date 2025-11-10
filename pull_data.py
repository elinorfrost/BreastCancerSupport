# pull_data.py
# Elinor Frost
# This file can be used to extract post information from a webpage. The data is sent to a json file.

# Starter code from codecademy's https://www.youtube.com/watch?v=b8q98xvyIqg
import requests
import bs4


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

def main(url):
    # css selectors for desired content
    css_selectors = {
        "post_body": '#__next > div > main > div.sc-64ce13e7-0.bgfGvQ > div.sc-64ce13e7-1.fDANYB > div > section:nth-child(2) > div.sc-7c31747b-1.gbAPbK.js-post-body p',
        "post_date": '#__next > div > main > div.sc-64ce13e7-0.bgfGvQ > div.sc-64ce13e7-1.fDANYB > div.sc-94bfdeac-0.kaVveJ > header > div > div:nth-child(2) > time',
        "num_comments": '#responses > div.sc-ccc13ae4-1.fFJXeU'
        # #__next > div > main > div.sc-64ce13e7-0.bgfGvQ > div.sc-64ce13e7-1.fDANYB > div > div.sc-64ce13e7-5.hqmKsY > div:nth-child(1) > div > div > div:nth-child(2) > a
    }

    # make a soup object of the page
    soup = bs4.BeautifulSoup(extract_source(url), "html.parser")

    # extract identifiers from url
    post_content = url.split("/")
    forum = post_content[-4]
    post_name = post_content[-2:]
    post_id = post_name[0]
    post_title = str(post_name[-1])


    # add content into a dictionary
    post = {
        "id": post_id,
        "forum": forum,
        "title": post_title,
        "content": str(find_with_css(soup, css_selectors["post_body"]).pop()).strip("<p>").strip(" </").replace("\u2019", "'"),
        "date": str(find_with_css(soup, css_selectors["post_date"])).split('datetime="')[-1].split('">')[0].split('.')[0]
        #"username": str(soup.find(class_="sc-18c93b1d-2 bIGrQn author")).split(">")[-2].split("<")[0],
        #"num_comments": int(str(find_with_css(soup, css_selectors["num_comments"])).split(">")[-2].split(" ")[0])
    }
    try:
        username = str(soup.find(class_="sc-18c93b1d-2 bIGrQn author")).split(">")[-2].split("<")[0]
        post["username"] = username
    except(IndexError):
        post["username"] = None

    try:
        num_comments = int(str(find_with_css(soup, css_selectors["num_comments"])).split(">")[-2].split(" ")[0])
        post["num_comments"] = num_comments
    except(IndexError):
        post["num_comments"] = 0

    # print(post)
    return(post)

if __name__ == "__main__":
    main()

