#!/usr/bin/python3
"""Function to query all hot list posts"""
import requests


def top_ten(subreddit):
    """Print the tittles of 10 hot post"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Google Chrome Version 81.0.4044.129"}
    params = {"limit": 10}
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code == 404:
        print(None)
        return
    results = res.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
