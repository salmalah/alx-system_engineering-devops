#!/usr/bin/python3
"""Reddit API"""

import requests
from collections import defaultdict

def count_words(subreddit, word_list, after="", word_count=None):
    """Count occurrences of words in subreddit titles"""

    if word_count is None:
        word_count = defaultdict(int)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after}
    headers = {'user-agent': 'bhalut'}

    response = requests.get(url, params=params, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for topic in data['data']['children']:
            title_words = topic['data']['title'].lower().split()
            for word in word_list:
                word_count[word.lower()] += title_words.count(word.lower())

        after = data['data']['after']
        if after is None:
            sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_word_count:
                if count > 0:
                    print(f"{word.lower()}: {count}")
        else:
            count_words(subreddit, word_list, after, word_count)
