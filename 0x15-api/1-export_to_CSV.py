#!/usr/bin/python3
"""
Summarize an employee's TODO list and write it to a file as a CSV
"""
import argparse
import csv
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
    dest = '.'.join([str(args.id), 'csv'])
    user = requests.get(ROUTES['users'](str(args.id)), timeout=5).json()
    todo = requests.get(ROUTES['todos'](str(args.id)), timeout=5).json()
    data = [[str(args.id), user['username'], task['completed'], task['title']]
            for task in todo]
    with open(dest, 'w', newline='') as ostream:
        csv.writer(ostream, quoting=csv.QUOTE_ALL).writerows(data)
