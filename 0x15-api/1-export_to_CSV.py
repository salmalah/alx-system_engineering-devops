#!/usr/bin/python3
"""
extend your Python script to export data in the CSV format
"""
import requests
import csv
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    emp_id = sys.argv[1]

    url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)
    user_response = requests.get(url_user)

    if user_response.status_code != 200:
        print("Error: Unable to fetch user data from the API")
        sys.exit(1)

    user_data = user_response.json()
    emp_name = user_data.get('name', 'Unknown')

    tasks_url = 'https://jsonplaceholder.typicode.com/todos'
    tasks_params = {'userId': emp_id}
    tasks_response = requests.get(tasks_url, params=tasks_params)

    if tasks_response.status_code != 200:
        print("Error: Unable to fetch tasks data from the API")
        sys.exit(1)

    todos = tasks_response.json()

    csv_f = '{}.csv'.format(emp_id)
    with open(csv_f, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            csv_writer.writerow([emp_id, emp_name, task['completed'], task['title']])

    print("CSV file '{}' has been created.".format(csv_f))

