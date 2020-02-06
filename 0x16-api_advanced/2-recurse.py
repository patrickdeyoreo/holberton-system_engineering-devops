#!/usr/bin/python3
"""
Get the titles of all the hot posts for a given subreddit
"""
import requests

URL = 'https://www.reddit.com/r/{}/hot.json'
USER_AGENT = 'Mozilla/5.0 (Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'


def recurse(subreddit, titles=[], **kwargs):
    """
    Query reddit for all hot posts of a subreddit
    """
    params = {
        'after': kwargs.get('after'),
        'count': kwargs.get('count', 0),
        'limit': kwargs.get('limit', 100)
    }
    r = requests.get(
        URL.format(subreddit),
        headers={'User-Agent': USER_AGENT},
        params=params,
        allow_redirects=False,
        timeout=30
    )
    if r.status_code == 200:
        results = r.json()['data']
        titles.extend(hot['data']['title'] for hot in results['children'])
        if results['after'] is not None:
            params['after'] = results['after']
            params['count'] += params['limit']
            kwargs.update(params)
            return recurse(subreddit, titles, **kwargs)
        return titles
    return None
