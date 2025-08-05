import requests

def post_data(url, data):
    response = requests.post(url, json=data)  
    if response.status_code == 201:  
        return response.json()
    else:
        return {"error": f"Status code {response.status_code}"}

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "title": "omar",
        "body": "1234",
        "userId": 1 
    }
    response = post_data(url, data)
    print(response)




# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "title": "omar",
#     "body": "1234"
# }

# response = requests.post(url, data=data)

# print(response.text)_data(url, data)