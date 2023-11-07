#!/usr/bin/python3
""" recursivly getting hot topics """
import requests


def recurse(subreddit, hot_list=None, after=None):
    if subreddit is None or type(subreddit) is not str:
        return None
    if hot_list is None:
        hot_list = []
    apiUrl = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyCoolReqName/1.0 (by /u/ReplyAdventurous5909)"}

    params = {"after": after}

    resp = requests.get(apiUrl, headers=headers,
                            params=params, allow_redirects=False)
    if resp.status_code == 200:
        data = resp.json()
        children = data["data"]["children"]

        for child in children:
            hot_list.append(child["data"]["title"])

        after = data["data"]["after"]
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    elif resp.status_code == 404:
        return None
    else:
        return None
