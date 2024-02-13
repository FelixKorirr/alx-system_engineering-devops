#!/usr/bin/python3
"""This script contains the function top_ten"""

import requests
from sys import argv


def top_ten(subreddit):
    """Returns the first ten posts for a subreddit"""

    usr = {'User-Agent': 'Lizzie'}
    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit), headers=usr).json()
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
