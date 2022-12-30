import requests

r = requests.post('http://127.0.0.1:5000/employee', data={'username': 'mike'})
print(r.text)

r = requests.put('http://127.0.0.1:5000/employee', data={'username': 'mike', 'new_name': 'hoge'})
print(r.text)

r = requests.delete('http://127.0.0.1:5000/employee', data={'username': 'mike'})
print(r.text)

