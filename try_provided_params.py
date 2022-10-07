import json

import requests

url = "http://127.0.0.1:10001/perform_query"

# headers = {"Content-Type": "application/json"}

payload = {
   'file_name': 'apache_logs.txt',
   'cmd1': 'regex',
   'value1': 'images/\\w+\\.png',
   'cmd2': 'sort',
   'value2': 'asc'
}

response = requests.request("POST", url, json=payload)
print(response.text)
