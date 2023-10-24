
#!/usr/bin/python3
"""script that export data to JSON file"""

import requests as req
import sys
import json

if __name__ == '__main__':
    employeeId = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + employeeId

    res = req.get(url)
    username = res.json().get('username')

    todo_url = url + "/todos"
    res = req.get(todo_url)
    tasks = res.json()

    dictionary = {employeeId: []}
    for task in tasks:
        dictionary[employeeId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })

    with open('{}.json'.format(employeeId), 'w') as filename:
        json.dump(dictionary, filename)
