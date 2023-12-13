
import requests


url = "https://jsonplaceholder.typicode.com/users"


response = requests.get(url)


import requests


url = "https://jsonplaceholder.typicode.com/users"


response = requests.get(url)


if response.status_code == 200:

    users = response.json()


    sorted_users = sorted(users, key=lambda x: x['name'].split()[0])


    print("Here's a list of the users sorted alphabetically by their first name : ")
    print("-----")
    for user in sorted_users:
        print(f"User ID: {user['id']}")
        print(f"Name: {user['name']}")
        print(f"Username: {user['username']}")
        print(f"Email: {user['email']}")
        print(f"Address: {user['address']['street']}, {user['address']['suite']}, {user['address']['city']}")
        print("-----")  # Separator between users

else:

    print(f"Failed to retrieve user data. Status code: {response.status_code}")



