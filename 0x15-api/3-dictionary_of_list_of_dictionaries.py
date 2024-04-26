#!/usr/bin/python3
''' Script that uses rest API to return a todo list'''
import json
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    main_url = f"{url}todos"
    user_url = f"{url}users"

    response = requests.get(main_url)
    response2 = requests.get(user_url)
    response = response.json()
    response2 = response2.json()

    users_id = []
    username = {}
    for i in response2:
        users_id.append(i['id'])
        username[i['id']] = i['username']
    formatted_data = {
            x: [{"username": username[x],
                 "task": i["title"],
                 "completed": i["completed"]}
                for i in response if i['userId'] == x] for x in users_id
            }
    json_string = json.dumps(formatted_data)

    with open('todo_all_employees.json', 'w+') as f:
        f.write(json_string)
