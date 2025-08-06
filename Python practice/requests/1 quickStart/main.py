import requests
from requests.exceptions import Timeout
import os

def WebGet(url):
    try:
        response = requests.get(url, timeout=1)
        print(response.ok)
        print(response.status_code)

        # file write
        file_path = r'L:\Programming\Python\All-Main Problem Solving\Python practice\requests\1 quickStart\python.html'
        with open(file_path, "w+", encoding='utf-8') as file:
            file.write(response.text)

    except Timeout as e:
        print("Timeout occurred:", str(e))
    except requests.RequestException as e:
        print("Request failed:", str(e))

WebGet('http://python.org')
