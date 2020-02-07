#!/usr/bin/python3
"""
Show number of occurrences of keywords in hot post titles (case-insensitive)
"""
import re
import requests

URL = 'https://www.reddit.com/r/{}/hot.json'
USER_AGENT = 'Mozilla/5.0 (Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'


def count_words(subreddit, word_list, **kwargs):
    """
    Query reddit for hot posts and print total occurrences of each keyword
    """
    totals = kwargs.setdefault('totals', dict.fromkeys(word_list, 0))
    params = {
        'after': kwargs.setdefault('after'),
        'limit': kwargs.setdefault('limit', 100),
    }
    r = requests.get(
        URL.format(subreddit),
        headers={'User-Agent': USER_AGENT},
        params=params,
        allow_redirects=False,
        timeout=30,
    )
    if r.status_code == 200:
        results = r.json()['data']
        titles = [post['data']['title'] for post in results['children']]
        for key in totals:
            for title in titles:
                totals[key] += len(
                    re.findall(r'(?:^| )' + key + '(?:$| )', title, re.I)
                )
        if results['after'] is not None:
            kwargs['after'] = results['after']
            return count_words(subreddit, [], **kwargs)
        keys = filter(totals.get, totals)
        for key in sorted(keys, key=lambda k: (-totals[k], k)):
            print('{}: {}'.format(key, totals[key]))
