#!/usr/bin/python3
"""A recursive function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list containing titles
    of all hot articles for a subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    r = response.json().get("data")
    after = r.get("after")
    count += r.get("dist")
    for x in r.get("children"):
        hot_list.append(x.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
