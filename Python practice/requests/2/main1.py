import requests

url = "https://httpbin.org/post"
data = {
    "username": "omar",
    "password": "1234"
}

response = requests.post(url, data=data)

print(response.text)