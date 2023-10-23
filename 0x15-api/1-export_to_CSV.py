#!/usr/bin/python3
"""
extend your Python script to export data in the CSV format
"""
import csv
import requests
import argv from sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()
    un = user_id.get("username")

    with open("{}.csv".format(argv[1]), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for m in todos:
            writer.writerow([argv[1], un, m["completed"], m["title"]])
