import requests

data = {"number": "167",
        "answer": "float64",
        "user": "a.barberin"}
r = requests.post("http://34.163.196.38/", data=data)
print(r.text)
