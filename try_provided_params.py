import json

import requests

url = "http://127.0.0.1:10001/perform_query"

# headers = {"Content-Type": "application/json"}

payload={
  'file_name': 'apache_logs.txt',
  'cmd1': 'map',
  'value1': '0',
  'cmd2': 'unique',
  'value2': ''
}

response = requests.request("POST", url, json=payload)
print(response.text)