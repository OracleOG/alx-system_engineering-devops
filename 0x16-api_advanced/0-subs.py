#!/usr/bin/python3
"""This module defines how API calls are made and maintained"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of total subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'user_agent':'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    data = response.json()
    if 'data' not in data:
        return 0
    if 'subscribers' not in data.get('data'):
        return 0
    return data['data']['subscribers'] 

