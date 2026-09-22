import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "abc"
USERNAME = "abc"
GRAPH_ID = "abc"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Working Time",
    "unit": "minutes",
    "type": "int",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()
print(today.strftime("%Y%m%d"))

requests_body = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "20",
}

put_body = {
    "quantity": "15",
}


# post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# response = requests.post(url=post_endpoint, json=requests_body, headers=headers)
# print(response.text)

put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20260921"

# response = requests.put(url=put_endpoint, json=put_body, headers=headers)
# print(response.text)

# response = requests.delete(url=put_endpoint, headers=headers)
# print(response.text)

