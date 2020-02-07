#!/usr/bin/python3
"""
Show number of occurrences of keywords in hot post titles (case-insensitive)
"""
import re
import requests

URL = 'https://www.reddit.com/r/{}/hot.json'


def count_words(subreddit, words, totals=None, after=None):
    """
    Query reddit for hot posts and print total occurrences of each keyword
    """
    r = requests.get(
        URL.format(subreddit),
        headers={'User-Agent': 'Mozilla/5.0'},
        params={'after': after, 'limit': 100},
        allow_redirects=False,
    )
    if r.status_code == 200:
        totals = totals or dict.fromkeys(words, 0)
        result = r.json().get('data', {})
        titles = [
            hotpost.get('data', {}).get('title', '') for
            hotpost in result.get('children', [])
        ]
        for key in totals:
            for title in titles:
                totals[key] += len(
                    re.findall(r'(?:^| )' + key + '(?:$| )', title, re.I)
                )
        if result.get('after') is None:
            keys = filter(totals.get, totals)
            for key in sorted(keys, key=lambda k: (-totals[k], k)):
                print('{}: {}'.format(key, totals[key]))
        else:
            count_words(subreddit, words, totals, result.get('after'))
