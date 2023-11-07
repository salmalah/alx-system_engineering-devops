#!/usr/bin/python3
"""
Recursivly getting hot topics
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    if subreddit is None or not isinstance(subreddit, str):
        return None
    apiUrl = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"after": after}
    headers = {"User-Agent": "MyCoolReqName/1.0 (by /u/ReplyAdventurous5909)"}
    response = requests.get(apiUrl, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        children = data["data"]["children"]

        for child in children:
            hot_list.append(child["data"]["title"])

        after = data["data"]["after"]
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    elif response.status_code == 404:
        return None
    else:
        return None

