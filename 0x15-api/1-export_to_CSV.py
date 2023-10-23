#!/usr/bin/python3
"""
Exports todo list information for a given employee ID in the CSV format
"""
import csv
import requests
import sys

if __name__ == "__main__":
    uid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    userId = requests.get(url + "users/{}".format(uid)).json()
    todos = requests.get(url + "todos", params={"userId": uid}).json()
    un = userId.get("username")

    with open("{}.csv".format(uid), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow([uid, un, t["completed"], t["title"]])
