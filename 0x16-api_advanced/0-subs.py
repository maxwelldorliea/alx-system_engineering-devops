#!/usr/bin/python3
"""ALX SE API Module."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers of a subreddit."""
    header = {
            'User-Agent': 'MyBot/1.0'
            }
    url = 'https://reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    return 0
