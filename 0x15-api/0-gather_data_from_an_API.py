#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)
    emp_id = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print("Error: Unable to fetch user data from the API")
        sys.exit(1)

    user_data = user_response.json()
    employee_name = user_data.get('name', 'Unknown')
    tasks_url = 'https://jsonplaceholder.typicode.com/todos'
    tasks_params = {'userId': emp_id}
    tasks_response = requests.get(tasks_url, params=tasks_params)

    if tasks_response.status_code != 200:
        print("Error: Unable to fetch tasks data from the API")
        sys.exit(1)

    todos = tasks_response.json()

    completed_tasks = [todo for todo in todos if todo['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_completed_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task['title']))
