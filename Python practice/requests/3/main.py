import requests
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "omar",
    "body": "1234"
}

response = requests.post(url, data=data)

print(response.text)