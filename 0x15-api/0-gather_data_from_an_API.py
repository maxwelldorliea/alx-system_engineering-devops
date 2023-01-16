#!/usr/bin/python3
"""ALX SE API INTRO."""
from sys import argv
import requests


def main() -> int:
    """Return information about a user TODO list progress."""
    base_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    todo_url = '{}/todos'.format(base_url)
    res = requests.get(todo_url)
    if res.status_code == 200:
        res = res.json()
        employee_name = requests.get(base_url).json().get('name')
        completed_tasks = [val for val in res if val["completed"]]
        number_of_done_taskS = len(completed_tasks)
        total_number_of_taskS = len(res)
        print('Employee {} is done with tasks({}/{}):'.format(
            employee_name, number_of_done_taskS,
            total_number_of_taskS))
        for task in completed_tasks:
            print(f'\t {task.get("title")}')
    return 0


if __name__ == '__main__':
    main()
