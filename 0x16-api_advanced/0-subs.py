#!/usr/bin/python3
"""Function to query number of subscribers"""
import requests as req


def number_of_subscribers(subreddit):
    """return total number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    res = req.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        return (0)
    results = res.json().get("data")
    return results.get("subscribers")
