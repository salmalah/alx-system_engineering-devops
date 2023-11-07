#!/usr/bin/python3
"""
100-count
"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    if subreddit is None or not isinstance(subreddit, str):
        return

    apiUrl = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 100, 'after': after}
    headers = {"User-Agent": "MyCoolReqName/1.0 (by /u/ReplyAdventurous5909)"}

    resp = requests.get(apiUrl, params=params, headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        posts = data.get('data', {}).get('children', [])

        for post in posts:
            t = post['data'].get('title', '').lower()
            for w in word_list:
                if w.lower() in t and not t.startswith(w.lower() + '.') \
                        and not t.startswith(w.lower() + '!') \
                        and not t.startswith(w.lower() + '_'):
                    word_count[w] = word_count.get(w, 0) + t.count(w.lower())

        after = data.get('data', {}).get('after')
        if after:
            count_words(subreddit, word_list, after, word_count)
        else:
            sortd_w_c = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sortd_w_c:
                print("{}: {}".format(word.lower(), count))
    else:
        return
