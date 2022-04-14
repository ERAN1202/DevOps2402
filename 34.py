from datetime import datetime
print(datetime.now())

import requests
response = requests.get("http://github.com")
print(response.text)
if response.status_code == 200:
    print("github is up and runnig")

response = requests.get("http://api.github.com/users/avielb")
print(response.json()["login"])
#אתר pipy האתר של ה package manager
response = requests.get("http://api.github.com/users/avielb/repos")
print(response.json())

for repo in response.json():
    print(repo["full_name"])