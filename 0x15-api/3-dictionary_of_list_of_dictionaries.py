#!/usr/bin/python3
"""Python script to export data in the JSON format"""

import requests as req
import sys
import json


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    res = req.get(url)
    users = res.json()

    dictionary = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        res = req.get(url)
        tasks = res.json()
        dictionary[user_id] = []
        for task in tasks:
            dictionary[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)
