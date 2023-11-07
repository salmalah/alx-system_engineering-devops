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
            title = post['data'].get('title', '').lower()
            for word in word_list:
                if word.lower() in title and not title.startswith(word.lower() + '.') and not title.startswith(word.lower() + '!') and not title.startswith(word.lower() + '_'):
                    word_count[word] = word_count.get(word, 0) + title.count(word.lower())

        after = data.get('data', {}).get('after')
        if after:
            count_words(subreddit, word_list, after, word_count)
        else:
            sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0].lower()))
            for word, count in sorted_word_count:
                print("{}: {}".format(word.lower(), count))
    else:
        return
