#!/usr/bin/python3
"""Script that export data in csv file"""

import requests as req
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + employeeId

    res = req.get(url)
    username = res.json().get('username')

    todo_url = url + "/todos"
    res = req.get(todo_url)
    tasks = res.json()

    with open('{}.csv'.format(employeeId), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employeeId, username, task.get('completed'),
                               task.get('title')))
