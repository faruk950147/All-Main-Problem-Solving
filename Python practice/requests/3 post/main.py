import requests

def post_data(url, data):
    response = requests.post(url, data=data)
    return response.json()

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "title": "omar",
        "body": "1234"
    }
    response = post_data(url, data)
    print(response)



# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "title": "omar",
#     "body": "1234"
# }

# response = requests.post(url, data=data)

# print(response.text)