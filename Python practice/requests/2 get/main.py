
import requests
from requests.exceptions import Timeout

# def get_data(url):
#     response = requests.get(url, timeout=5)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None


# if __name__ == "__main__":
#     url = "https://jsonplaceholder.typicode.com/todos/1"
#     data = get_data(url)
#     print(data)


url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url, timeout=5)
data = response.json()
print(data)
print(data['title'])
print(data['completed'])
print(data['userId'])
print(data['id'])


