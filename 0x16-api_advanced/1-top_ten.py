#!/usr/bin/python3
"""This module defines how API calls are made and maintained"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed
    for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'user_agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return
    data = response.json()
    posts = data['data']['children']

    if len(posts) == 0:
        print(None)
    else:
        for post in posts:
            print(post['data']['title'])
