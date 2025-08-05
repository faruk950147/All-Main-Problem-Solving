import requests

def auth(url, data):
    response = requests.get(url, data)
    return response.json()

# url = "https://httpbin.org/post"
# data = {
#     "username": "omar",
#     "password": "1234"
# }

# response = requests.post(url, data=data)

# print(response.text)