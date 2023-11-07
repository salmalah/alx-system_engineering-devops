#!/usr/bin/python3
""" recursivly getting hot topics """
import requests


def recurse(subreddit, title_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "my_script:reddit_api:v1.0.0 (by /u/Nickname-Pending1)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    resp = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)
    if resp.status_code == 404:
        return None

    result = resp.json().get("data")
    after = result.get("after")
    count += result.get("dist")
    for c in result.get("children"):
        title_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, title_list, after, count)
    return title_list
