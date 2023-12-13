# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests

# The API endpoint
url = "https://jsonplaceholder.typicode.com/users"

# A GET request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
import requests

# The API endpoint
url = "https://jsonplaceholder.typicode.com/users"

# A GET request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    users = response.json()

    # Sort users by first name alphabetically
    sorted_users = sorted(users, key=lambda x: x['name'].split()[0])

    # Iterate through each sorted user and print relevant information
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
    # Print an error message if the request was not successful
    print(f"Failed to retrieve user data. Status code: {response.status_code}")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
