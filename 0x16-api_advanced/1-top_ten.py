#!/usr/bin/python3
"""
module to define the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    if subreddit is None or type(subreddit) is not str:
        return 0
    apiUrl = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "MyCoolReqName/1.0 (by /u/ReplyAdventurous5909)"}
    resp = requests.get(apiUrl, headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        if "data" in data and "children" in data["data"]:
            for post in data["data"]["children"]:
                title = post["data"]["title"]
                print(title)
    else:
        print(None)
