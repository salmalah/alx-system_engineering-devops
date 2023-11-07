#!/usr/bin/python3
""" recursivly getting hot topics """
import requests


def count_words(subreddit, word_list, count_dict={}, after="", count=0):
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
    try:
        result = resp.json()
        if resp.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    result = result.get("data")
    after = result.get("after")
    count += result.get("dist")
    for c in result.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if count_dict.get(word) is None:
                    count_dict[word] = times
                else:
                    count_dict[word] += times

    if after is None:
        if len(count_dict) == 0:
            print("")
            return
        count_dict = sorted(count_dict.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in count_dict]
    else:
        count_words(subreddit, word_list, count_dict, after, count)
