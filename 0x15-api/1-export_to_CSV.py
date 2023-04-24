#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: User ID not provided.")
        sys.exit(1)
    
    url = 'https://jsonplaceholder.typicode.com/'

    userid = sys.argv[1]
    user = '{}users/{}'.format(url, userid)
    try:
        res = requests.get(user)
        res.raise_for_status()
        json_o = res.json()
        name = json_o.get('username')

        todos = '{}todos?userId={}'.format(url, userid)
        res = requests.get(todos)
        res.raise_for_status()
        tasks = res.json()
        l_task = []
        for task in tasks:
            l_task.append([userid,
                           name,
                           task.get('completed'),
                           task.get('title')])

        filename = '{}.csv'.format(userid)
        with open(filename, mode='w') as employee_file:
            employee_writer = csv.writer(employee_file,
                                         delimiter=',',
                                         quotechar='"',
                                         quoting=csv.QUOTE_ALL)
            for task in l_task:
                employee_writer.writerow(task)
    except requests.exceptions.HTTPError as err:
        print("Error:", err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print("Error:", err)
        sys.exit(1)

