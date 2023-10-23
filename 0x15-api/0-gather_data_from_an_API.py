#!/usr/bin/python3
"""
returns information about TODO list progress for a given employee ID
"""
import requests
from sys import argv


if __name__ == "__main__":
    """main api method"""
    url = "https://jsonplaceholder.typicode.com/"
    user_id = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()
    emp = user_id.json()
    todo = todos.json()
    n = [i for i in todo if i.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        emp.get("name"), len(n), len(todo)))
    for t in n:
        print('\t {}'.format(t.get("title")))
