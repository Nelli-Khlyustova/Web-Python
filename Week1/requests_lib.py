import requests
import json

r = requests.get('http://httpbin.org/get')
print(r.text)

r = requests.post('http://httpbin.org/post')
print(r.text)

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.text)

r = requests.post('http://httpbin.org/post', data={'key': 'value'})
print(r.text)

url = 'http://httpbin.org/post'
r = requests.post(url, data=json.dumps({'key': 'value'}))
r = requests.post(url, json={'key': 'value'})
print(r.text)
