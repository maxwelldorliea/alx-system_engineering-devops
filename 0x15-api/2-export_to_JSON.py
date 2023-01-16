#!/usr/bin/python3
"""ALX SE API INTRO."""
from sys import argv
import json
import requests


def main() -> int:
    """Save information about a user TODO list progress to a json file."""
    base_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    todo_url = '{}/todos'.format(base_url)
    res = requests.get(todo_url)
    if res.status_code == 200:
        res = res.json()
        name = requests.get(base_url).json().get('username')
        filename = "{}.json".format(argv[1])
        with open(filename, 'w', encoding='utf8') as json_file:
            obj_props = []
            user_id = ''
            for task in res:
                obj = {
                        "task": task["title"],
                        "completed": task["completed"],
                        "username": name}
                user_id = task["userId"]
                obj_props.append(obj)
            json.dump({user_id: obj_props}, json_file)

    return 0


if __name__ == '__main__':
    main()
