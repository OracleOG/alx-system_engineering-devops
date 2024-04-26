#!/usr/bin/python3
''' Script that uses rest API to return a todo list'''
import json
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = int(sys.argv[1])
    main_url = f"{url}todos?userId={user_id}"
    user_url = f"{url}users?id={user_id}"

    response = requests.get(main_url)
    response2 = requests.get(user_url)
    response = response.json()
    response2 = response2.json()

    name = None
    for i in response2:
        if i['id'] == user_id:
            name = i['username']

    filename = f'{user_id}.json'

    formatted_data = {
            user_id: [{"task": i["title"],
                       "completed": i["completed"],
                       "username": name}
                      for i in response if i['userId'] == user_id]
        }
    json_string = json.dumps(formatted_data)

    with open(filename, 'w+') as f:
        f.write(json_string)
