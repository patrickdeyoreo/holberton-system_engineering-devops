#!/usr/bin/python3
"""
Summarize an employee's TODO list progress
"""
import argparse
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
    user = requests.get(ROUTES['users'](str(args.id)), timeout=5).json()
    todo = requests.get(ROUTES['todos'](str(args.id)), timeout=5).json()
    completed = [task for task in todo if task.get('completed') is True]
    print('Employee {name} is done with tasks({done}/{total}):'.format(
        name=user.get('name'), done=len(completed), total=len(todo)
    ))
    for task in completed:
        print('\t {}'.format(task['title']))
