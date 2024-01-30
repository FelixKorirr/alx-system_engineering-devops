#!/usr/bin/python3
""" Python Script to export data in Json format"""
import csv
import json
import requests
import sys


if __name__ == '__main__':
    USER_ID = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    req = requests.get(user_url)
    USERNAME = req.json().get('username')
    task_url = user_url + '/todos'
    req = requests.get(task_url)
    all_tasks = req.json()

    dict_data = {USER_ID: []}
    for task in all_tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        dict_data[USER_ID].append({
                                  "task": TASK_TITLE,
                                  "completed": TASK_COMPLETED_STATUS,
                                  "username": USERNAME})
    with open('{}.json'.format(USER_ID), 'w') as file:
        json.dump(dict_data, file)
