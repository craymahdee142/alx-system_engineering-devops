#!/usr/bin/python3
"""Function to query all hot list posts"""
import requests


def recurse(subreddit, hot_list=[]):
    """Print the tittles of hot post"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Google Chrome Version 81.0.4044.129"}
    params = {"after": after, "count": count, "limit": 404}
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code == 404:
        return (None)
    results = res.json().get("data")
    after = results.get("after")
    count = results.get("count")
    for c in results.get("chi;dren"):
        hot_list.append(c.get(data).get("titles"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
