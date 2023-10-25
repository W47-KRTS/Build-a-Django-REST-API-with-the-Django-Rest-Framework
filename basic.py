# Build a Django REST API with the Django Rest Framework

import requests

# API - Application programing interface 
# kind of a url. there will be several endpoints in the client
# endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"

#use the api that is in this library
# API -> Method (function built into it)

get_response = requests.get(endpoint, json={"query":"Hello, brother!"}) # HTTP Request
print(get_response.text)  #print raw text response

# HTTP Request -> HTML 
# Rest API HTTP Request -> JSON -a web API allows your app to work with another app thru the web

# JavaScropt Object Notation (JSON)- almost a Python Dict - "json": null
#{
#  "args": {},
#  "data": "",
#  "files": {},
#  "form": {},
#  "headers": {
#    "Accept": "*/*",
#    "Accept-Encoding": "gzip, deflate",
#    "Host": "httpbin.org",
#    "User-Agent": "python-requests/2.31.0",
#    "X-Amzn-Trace-Id": "Root=1-6538b8d0-1f36d3e51ac737aa5def3c20"
#  },
#  "json": null,
#  "method": "GET",
#  "origin": "86.125.123.36",
#  "url": "https://httpbin.org/anything"
#}

print(get_response.json())

# now is a Python Dict
# {'args': {}, 'data': '', 'files': {}, 'form': {}, 
# 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, 
# 'deflate', 'Host': 'httpbin.org', 'User-Agent': 
# 'python-requests/2.31.0', 'X-Amzn-Trace-Id': 
# 'Root=1-6538bc1b-0b54882237383f1c11170034'}, 'json': None, 
# 'method': 'GET', 'origin': '86.125.123.36', 
# 'url': 'https://httpbin.org/anything'}

# json={"query":"Hello, brother!"} -> 'data': '{"query": "Hello, brother!"}'

print(get_response.status_code) # -> 200
