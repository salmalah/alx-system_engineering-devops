#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <employee ID>".format(sys.argv[0]))
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        emp_id
    )
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        emp_id
    )
    resp = requests.get(user_url)
    if resp.status_code != 200:
        print("Error: Unable to fetch user data")
        sys.exit(1)
    user = resp.json()
    emp_name = user.get("name")
    resp = requests.get(todos_url)
    if resp.status_code != 200:
        print("Error: Unable to fetch todos data")
        sys.exit(1)

    todos = resp.json()
    done_tasks = [t for t in todos if t.get("completed")]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            emp_name, len(done_tasks), len(todos)
        )
    )
    for t in done_tasks:
        print("\t {}".format(t.get("title")))
