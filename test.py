import requests

BASE = "https://mango-friends.herokuapp.com/"
# BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE+"helloworld/ivan/20")
print(response.json())
