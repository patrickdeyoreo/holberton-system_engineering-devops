#!/usr/bin/python3
"""
Print the titles of the top ten posts for a given subreddit
"""
import requests

URL = 'https://www.reddit.com/r/{}/hot.json'
USER_AGENT = 'Mozilla/5.0 (Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'


def top_ten(subreddit):
    """
    Query reddit for the top ten posts of a subreddit
    """
    resp = requests.get(
        URL.format(subreddit),
        headers={'User-Agent': USER_AGENT},
        params={'limit': 10},
        allow_redirects=False,
        timeout=10
    )
    if resp.status_code == 200:
        for post in resp.json()['data']['children']:
            print(post['data']['title'])
    else:
        print('None')
