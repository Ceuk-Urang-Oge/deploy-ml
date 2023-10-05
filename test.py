import requests

res = requests.post('http://127.0.0.1:5000/', files={'file': open('./data/three.png', 'rb')})

print(res.json())