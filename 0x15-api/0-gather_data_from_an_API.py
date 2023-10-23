#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_url = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos _url = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [x.get("title") for x in todos_url if x.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user_url.get("name"), len(completed), len(todos)))
    [print("\t {}".format(n)) for n in completed]
