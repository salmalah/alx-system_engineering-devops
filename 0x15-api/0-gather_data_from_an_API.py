#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID
"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get("{}/users/{}".format(url, employee_id))
    todos_response = requests.get("{}/todos?userId={}"
                                  .format(url, employee_id))

    employee_name = user_response.json().get('name')
    todos = todos_response.json()

    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo["completed"]]
    num_done_tasks = len(done_tasks)

    print("Employee {} is done with tasks(\
{}/{}):".format(employee_name, num_done_tasks, total_tasks))
    for task in done_tasks:
        print("\t {}".format(task['title']))
