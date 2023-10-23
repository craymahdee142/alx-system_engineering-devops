#!/usr/bin/python3
"""Script that returns employee info using REST API"""

import requests as req
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    # make request to fetch employee info
    res = req.get(url + "users/{}".format(employee_id)).json()
    # make request to fetch task for employee
    tasks = req.get(url + "todos", params={"userId": employee_id}).json()

    # filter completed task
    completed_tasks = [task["title"] for task in tasks if task["completed"]]
    # extrack employee name and count
    employee_name = res.get("name")
    num_of_completed = len(completed_tasks)
    num_of_task = len(tasks)

    print(f"Employee {employee_name} is done with tasks "
          f"({num_of_completed}/{num_of_task}):")
    [print(f"\t {task}") for task in completed_tasks]
