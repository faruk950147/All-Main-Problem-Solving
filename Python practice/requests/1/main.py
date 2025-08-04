import requests
# GET request
response = requests.get("https://github.com/")
# print response status code
print(response.ok)
print(response.status_code)
print(response.headers)
print(response.text)
print(response.content)
print(response.cookies)
print(response.url)
print(response.history)
print(response.request)
print(response.raw)
print(response.elapsed)
print(response.links)
print(response.close())
print(response.reason)
print(response.request)
print(type(response))
print(response.raise_for_status())
print(response.request)
# print response json and pretty print
# print(response.json())

# POST request
# response = requests.post("https://github.com/", json={"name": "John", "age": 30})
# # print response status code
# print(response.status_code)
# # print response json and pretty print
# print(response.json())
