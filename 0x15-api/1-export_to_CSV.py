#!/usr/bin/python3
"""ALX SE API INTRO."""
from sys import argv
import csv
import requests


def main() -> int:
    """Save information about a user TODO list progress to a csv file."""
    base_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    todo_url = '{}/todos'.format(base_url)
    res = requests.get(todo_url)
    if res.status_code == 200:
        res = res.json()
        name = requests.get(base_url).json().get('username')
        filename = "{}.csv".format(argv[1])
        with open(filename, 'w', encoding='utf8') as csv_file:
            csv_file = csv.writer(
                    csv_file, delimiter=',',
                    quoting=csv.QUOTE_ALL, quotechar='"')
            for task in res:
                csv_file.writerow(
                        [
                            task['userId'], name,
                            task['completed'], task['title']])
    return 0


if __name__ == '__main__':
    main()
