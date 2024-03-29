#!/usr/bin/python3
"""
This script gathers employee data from API
"""

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            req = requests.get('{}/users/{}'.format(REST_API, id)).json()
            task_req = requests.get('{}/todos'.format(REST_API)).json()
            employee_name = req.get('name')
            all_tasks = list(filter(lambda x: x.get('userId') == id, task_req))
            completed = list(filter(lambda x: x.get('completed'), all_tasks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    employee_name,
                    len(completed),
                    len(all_tasks)
                )
            )
            if len(completed) > 0:
                for task in completed:
                    print('\t {}'.format(task.get('title')))
