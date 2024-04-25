#!/usr/bin/python3
''' Script that uses rest API to return a todo list'''
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    main_url = f"{url}todos?userId={user_id}"
    user_url = f"{url}users?id={user_id}"

    response = requests.get(main_url)
    response2 = requests.get(user_url)
    response = response.json()
    response2 = response2.json()
    comp_todo = []

    for todo in response:
        if todo['completed']:
            comp_todo.append(todo)
    total_todo = len(response)
    completed = len(comp_todo)
    print(f"Employee {response2[0]['name']} is done with tasks ({completed}/{total_todo}):")
    for x in comp_todo:
        print(f'\t {x["title"]}')
