# File that follows along with the web scraping tutorial to download xkcd comics
# from https://www.youtube.com/watch?v=87Gx3U0BDlo

import requests

import bs4

base_url = "https://xkcd.com/"
url = "https://xkcd.com/1"
# xkcd is cool because the last html page always ends in the # symbol
while "10" not in url:
    # ---PART 1: REQUEST AND SOUPIFY---
    # make request to web page
    response = requests.get(url)
    # print(response.content) # test

    # parse page to make it easier to use
    soup = bs4.BeautifulSoup(response.content, "html.parser")
    # print(soup) # test

    # ---PART 2: FIND URL OF IMAGE---
    img_element = soup.select("#comic img").pop() # target all images inside the comic div,
    # but .pop takes the only one, which is what we want
    # print(img_element)
    img_src = img_element["src"]
    img_src = "http:" + str(img_src)
    # print(img_src)

    # get name of file, which is last elt in html link
    img_name = img_src.split("/")[-1]

    # ---PART 3: DOWNLOAD THE COMIC
    response = requests.get(img_src)

    with open("comics/" + img_name, 'wb') as file: #wb means write bites
        file.write(response.content)

    # ---PART 4: FIND THE NEXT BUTTON
    # find things from an attribute
    next_a = soup.select(".comicNav a[rel='next']")[0]
    #print(next_a)
    next_href = next_a["href"] # pull out the next href
    url = base_url + str(next_href)
    print(url)
