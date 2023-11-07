#!/usr/bin/python3
"""
Recursivly getting hot topics
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    if subreddit is None or not isinstance(subreddit, str):
        return None
    
    apiUrl = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 100, 'after': after}
    headers = {"User-Agent": "MyCoolReqName/1.0 (by /u/ReplyAdventurous5909)"}

    resp = requests.get(apiUrl, params=params, headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        posts = data.get('data', {}).get('children', [])
        
        for post in posts:
            title = post['data'].get('title')
            if title:
                hot_list.append(title)
        
        after = data.get('data', {}).get('after')
        if after:
            recurse(subreddit, hot_list, after)
        
        return hot_list
    else:
        return None

