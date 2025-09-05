import requests

data = {"number": "85",
        "answer": "3",
        "user": "a.barberin"}
r = requests.post("http://34.163.196.38/", data=data)
print(r.text)
