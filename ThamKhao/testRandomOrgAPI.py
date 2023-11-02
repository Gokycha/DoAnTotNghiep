import requests
import json

raw_data = {
    "jsonrpc": "2.0",
    "method": "generateIntegers",
    "params": {
        "apiKey": "your-api-key",
        "n": 6,
        "min": 1,
        "max": 6,
        "replacement": True
    },
    'id':1
}

headers = {'Content-type': 'application/json','Content-Length': '200', 'Accept': 'application/json'}

data=json.dumps(raw_data)

response = requests.post(
    url='https://api.random.org/json-rpc/2/invoke',
    data=data,
    headers=headers
    )

print(response.text)