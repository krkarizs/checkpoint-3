import requests

response = requests.get("https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json")

data = response.json()
data_items = data["items"]

parameter_list = []

for i in data_items:
    parameter_list.append(i["parameter"])

with open("checkpoint.txt", "w") as x:
    for it in parameter_list:
        x.write(f"{it}\n")