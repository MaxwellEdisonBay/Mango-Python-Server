import requests

BASE = "https://test-ivanteslenko.herokuapp.com/"

response = requests.get(BASE+"helloworld/tsds/19")
print(response.json())
