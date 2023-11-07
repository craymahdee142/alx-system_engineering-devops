#!/usr/bin/python3
"""Function to print hot posts"""
import requests as req


def def top_ten(subreddit):
    """Print the tittles of hot post"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Google Chrome Version 81.0.4044.129"}
    params = {"limit": 10}
    res = req.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        print(""None)
        return (0)
    results = res.json().get("data")
    [print(c.get("data").get("titles")) for c in results.get("children")]
