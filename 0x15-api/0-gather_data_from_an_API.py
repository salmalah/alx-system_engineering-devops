#!/usr/bin/python3
"""
returns information about TODO list progress for a given employee ID
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()
    n = [i for i in todos if i.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user_id.get("name"), len(n), len(todos)))
    for t in n:
        print('\t {}'.format(t.get("title")))
