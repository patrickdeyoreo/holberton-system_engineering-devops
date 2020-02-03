#!/usr/bin/python3
"""
Summarize an employee's TODO list and write it to a file as a CSV
"""
import json
import requests

PREFIX = 'https://jsonplaceholder.typicode.com'
ROUTES = {
    'users': lambda user_id='': '/'.join([PREFIX, 'users', user_id]),
    'todos': lambda user_id='': '/'.join([PREFIX, 'users', user_id, 'todos'])
}
DEST = 'todo_all_employees.json'

if __name__ == '__main__':

    users = requests.get(ROUTES['users'](), timeout=5).json()
    data = []
    for user in users:
        user_id = str(user['id'])
        todo = requests.get(ROUTES['todos'](user_id), timeout=5).json()
        for task in todo:
            data.append({
                user_id: [{
                    "username": user['username'],
                    "task": task['title'],
                    "completed": task['completed'],
                } for task in todo]
            })
    with open(DEST, 'w') as ostream:
        ostream.write(json.dumps(data)[1:-1])
