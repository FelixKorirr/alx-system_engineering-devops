#!/usr/bin/python3
'''This script returns the number_of_subscribers for
a given subreddit'''
import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''Returns the number of subscribers for a subreddit'''

    usr = {'User-Agent': 'Lizzie'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=usr).json()
    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
