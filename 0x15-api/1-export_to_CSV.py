#!/usr/bin/python3
"""This script exports api to csv"""
import csv
import requests
import sys

if __name__ == '__main__':
    usr = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/' + usr
    req = requests.get(user_url)
    user_name = req.json().get('username')
    task = user_url + '/todos'
    req = requests.get(task)
    all_tasks = req.json()

    with open('{}.csv'.format(usr), 'w') as csvfile:
        for task in all_tasks:
            completed = task.get('completed')
            title_task = task.get('title')
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                usr, user_name, completed, title_task))
