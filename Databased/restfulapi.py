from urllib.request import urlopen
# the restful api will give us JSON data


import json

url = "https://jsonplaceholder.typicode.com/"

response = urlopen(url)

data = response.read()

print(type(data),data)



url = "https://jsonplaceholder.typicode.com/"

response = urlopen(url)

data = json.loads(response.read())

for post in data:
    (post,user,tittle,body) = data.readvalue()
    print("Post Id:",post["id"])
    print("User Id:",post["userid"])
    print("Tittle:",post["tittle"])
    print("Body:",post["body"])


