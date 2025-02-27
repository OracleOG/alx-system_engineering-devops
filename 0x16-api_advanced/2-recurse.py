#!/usr/bin/python3
"""This module defines how API calls are made and maintained"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """recursive function that queries the Reddit API and returns a
    list containing the titles of all hot articles for a given subreddit
    """
    if hot_list is None:
        hot_list = []
    
    # Build URL with pagination parameter if available
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"
    
    headers = {'user-agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None
    
    data = response.json()
    posts = data['data']['children']
    
    # Extract titles from current batch of posts
    for post in posts:
        hot_list.append(post['data']['title'])
    
    # Check if there are more posts to fetch
    after = data['data'].get('after')
    
    # If more posts exist, make recursive call with updated 'after' parameter
    if after:
        return recurse(subreddit, hot_list, after)
    
    # No more posts, return the complete list
    return hot_list