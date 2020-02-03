#!/usr/bin/python3
"""
Summarize an employee's TODO list and write it to a file as JSON
"""
import argparse
import json
import os
import requests
import sys

PREFIX = 'https://jsonplaceholder.typicode.com'
ROUTES = {
    'users': lambda user_id: '/'.join([PREFIX, 'users', user_id]),
    'todos': lambda user_id: '/'.join([PREFIX, 'users', user_id, 'todos'])
}

if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog=os.path.basename(sys.argv[0]))
    parser.add_argument('id', type=int, help='employee ID')
    args = parser.parse_args()
    dest = '.'.join([str(args.id), 'json'])
    user = requests.get(ROUTES['users'](str(args.id)), timeout=5).json()
    todo = requests.get(ROUTES['todos'](str(args.id)), timeout=5).json()
    data = {
        str(args.id): [{
            "task": task['title'],
            "completed": task['completed'],
            "username": user['username'],
        } for task in todo]
    }
    with open(dest, 'w') as ostream:
        json.dump(data, ostream)
