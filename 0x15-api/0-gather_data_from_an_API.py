#!/usr/bin/python3
"""ALX SE API INTRO."""
import requests
from sys import argv


def main() -> int:
    """Return information about a user TODO list progress."""
    BASE_URL = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    TODO_URL = f'{BASE_URL}/todos'
    res = requests.get(TODO_URL)
    if res.status_code == 200:
        res = res.json()
        EMPLOYEE_NAME = requests.get(BASE_URL).json().get('name')
        completed_tasks = [val for val in res if val["completed"]]
        NUMBER_OF_DONE_TASKS = len(completed_tasks)
        TOTAL_NUMBER_OF_TASKS = len(res)
        print('Employee {} is done with tasks({}/{}):'.format(
            EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
        for task in completed_tasks:
            print(f'     {task.get("title")}')
    return 0


if __name__ == '__main__':
    main()
