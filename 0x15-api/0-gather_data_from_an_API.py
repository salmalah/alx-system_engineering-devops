#!/usr/bin/python3
"""
returns information about TODO list progress for a given employee ID
"""
import requests
import sys


if __name__ == "__main__":
    uid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    userId = requests.get(url + "users/{}".format(uid)).json()
    todos = requests.get(url + "todos", params={"userId": uid}).json()
    done = [task for task in todos if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        userId.get("name"), len(done), len(todos)))
    for tasks in done:
        print("\t {}".format(tasks))
