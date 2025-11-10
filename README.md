# Breast Cancer Support
### Elinor Frost

### Overview
A project where I learn basic web scraping to collect data for potential machine learning or statistical modelling projects.
I plan to scrape user posts and comments from the *SHARE Metastatic Breast Cancer* page within *Health Unlocked*, a support forum for people to share their experiences and find community with individuals who experience similar disease and illnesses.

### Files
`pull_data.py`: a file to extract data from web pages. Creates dictionaries of posts, including the user, id, text, date, and number of comments.

`scratch.py`: a place to put code as I learn web scraping

`loop.py`: loops through pages of a health unlocked community archive and calls pull_data. Puts the dictionaries of posts into a json file.

### Bugs
- When pulling text content, there's sometimes unexpected characters denoting things like tildes or emojis.
- CSS selector strings are not the most reliable way to select content from the web page. They're working fine for now, but I don't know how they are finding the content because I don't know CSS.
- Only takes the 30 most recent posts for months with more than 30 posts. Posts are limited to 30 per page, and I haven't accounted for months with many pages.

### TODO:
- Want to extract comment content, rather than just the number of comments for each post.
- Could easily create a loop to go through multiple years with string manipulation for the URL. Could also loop through multiple communities. Not happy enough with the json format to pull lots of data yet.
- Need to change `loop.py` to loop through all the pages in a month when theres more than 30 posts.
