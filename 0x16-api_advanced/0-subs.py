#!/usr/bin/python3
"""
module 0-subs
"""
import requests


def number_of_subscribers(subreddit):
    if subreddit is None or type(subreddit) is not str:
        return 0
    apiUrl = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "MyCoolReqName/1.0 (by /u/ReplyAdventurous5909)"}

    resp = requests.get(apiUrl, headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        return data["data"]["subscribers"]
    else:
        return 0
