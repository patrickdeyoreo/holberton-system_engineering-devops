#!/usr/bin/python3
"""
Show number of occurrences of keywords in hot post titles (case-insensitive)
"""
import requests

URL = 'https://www.reddit.com/r/{}/hot.json'
USER_AGENT = 'Mozilla/5.0 (Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'


def count_words(subreddit, words, **kwargs):
    """
    Query reddit for hot posts and print total occurrences of each keyword
    """
    totals = kwargs.setdefault('totals', dict.fromkeys(words, 0))
    params = {
        'after': kwargs.setdefault('after'),
        'count': kwargs.setdefault('count', 0),
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
        for post in results['children']:
            words = post['data']['title'].split()
            words = [w.casefold() for w in words]
            for word in words:
                for key in totals:
                    if key.casefold() in words:
                        totals[key] += 1
        if results['after'] is not None:
            kwargs['after'] = results['after']
            kwargs['count'] += kwargs['limit']
            return count_words(subreddit, [], **kwargs)
        keys = filter(totals.get, totals)
        for key in sorted(keys, key=totals.get, reverse=True):
            print('{}: {}'.format(key, totals[key]))
