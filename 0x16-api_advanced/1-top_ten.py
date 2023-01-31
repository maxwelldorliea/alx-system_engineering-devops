#!/usr/bin/python3
"""ALX SE API Module."""
import requests


def top_ten(subreddit):
    """Print the title of the top ten post in a subreddit."""
    header = {
            'User-Agent': 'MyBot/1.0'
            }
    url = 'https://reddit.com/r/{}/top.json'.format(subreddit)
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        post_list = response.json()['data']['children']
        for idx, post in enumerate(post_list):
            print(post['data']['title'])
            if idx == 9:
                break
    else:
        print('None')
