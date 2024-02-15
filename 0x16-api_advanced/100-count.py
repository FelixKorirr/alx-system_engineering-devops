#!/usr/bin/python3
""" This module queries the Reddit API recursively"""


import requests


def count_words(subreddit, word_list, a='', w={}):
    """ A function that queries the Reddit API parses"""

    if not w:
        for word in word_list:
            if word.lower() not in w:
                w[word.lower()] = 0

    if a is None:
        wordict = sorted(w.items(), key=lambda x: (-x[1], x[0]))
        for word in wordict:
            if word[1]:
                print('{}: {}'.format(word[0], word[1]))
        return None

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'user-agent': 'redquery'}
    param = {'limit': 100, 'a': a}
    r = requests.get(url, headers=header, params=param,
                            allow_redirects=False)

    if r.status_code != 200:
        return None

    try:
        hot = r.json()['data']['children']
        aft = r.json()['data']['a']
        for post in hot:
            title = post['data']['title']
            lower = [word.lower() for word in title.split(' ')]

            for word in w.keys():
                w[word] += lower.count(word)

    except Exception:
        return None

    count_words(subreddit, word_list, aft, w)
