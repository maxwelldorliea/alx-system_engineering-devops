#!/usr/bin/python3
"""ALX SE API Module."""
import requests


def top_ten(subreddit):
    """Print the title of the top ten post in a subreddit."""
    header = {
            'User-Agent': 'MyBot/1.0'
            }
    param = {
            'limit': 10
            }
    url = 'https://reddit.com/r/{}/top.json'.format(subreddit)
    response = requests.get(url, params=param, headers=header)
    if response.status_code == 200:
        post_list = response.json()['data']['children']
        for post in post_list:
            print(post['data']['title'])
    else:
        print('None')
