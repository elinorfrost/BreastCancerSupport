# loop.py
# Elinor Frost
# This file loops through pages of a Health Unlocked website, calling functions from pull_data.py to extract data from each page.
import pull_data as pull
import bs4
import json

def main():
    # set first url
    base_url = "https://healthunlocked.com"
    month_base_url = base_url + "/pregnancy-parenting-support/posts/archive/2024/"

    # Several communities of interest
    # month_base_url = base_url + "/bashh/posts/archive/2024/"
    # month_base_url = base_url + "/share-metastatic-support/posts/archive/2024/"
    month_urls = []

    # add urls to list 
    for i in range(12):
        if i < 9:
            month_urls.append(month_base_url + "0" + str(i + 1) + "?page=1")
        else:
            month_urls.append(month_base_url + str(i + 1) + "?page=1")

    # collect all post urls
    all_urls = []

    # loop through each month of posts in the archive
    for url in month_urls:
        soup = bs4.BeautifulSoup(pull.extract_source(url), "html.parser")
        posts = soup.find_all(class_="sc-64ce13e7-6 enKsrL")

        # collect post urls from the current month
        urls = []
        for post in posts:
            link = post.find("a")["href"]
            link = base_url + link
            urls.append(link)

        # add all of this month's posts
        all_urls.extend(urls)

    print(f"Number of posts found: {len(all_urls)}")

    # extract info from each url in url_list
    data = []

    # TEST
    # for i in range(10):
    #     url = all_urls[i]
    #     data.append(pull.main(url))


    # Write data to json for all posts
    i = 0
    for url in all_urls:
        print(i)
        i += 1
        data.append(pull.main(url))


    with open("pregParentSupport2024.json", "w") as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    main()
