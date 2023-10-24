#!/usr/bin/python3
"""script that export data to JSON file"""


import json
import requests as req
import sys


# Define base URL
base_url = "https://jsonplaceholder.typicode.com/"


# Define a function to get user data
def get_user_data(user_id):
    user = req.get(f"{base_url}users/{user_id}").json()
    username = user.get("username")
    todos = req.get(f"{base_url}todos", params={"userId": user_id}).json()
    return user_id, username, todos


# Define a function to export data to JSON
def export_to_json(filename, data):
    with open(f"{filename}.json", "w") as jsonfile:
        json.dump({data[0]: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": data[1]
        } for task in data[2]]}, jsonfile)


if __name__ == "__main__":
    user_id = sys.argv[1]

    # Get user data
    user_data = get_user_data(user_id)
    # Export data to JSON
    export_to_json(user_id, user_data)
