import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = ""
TOKEN = ""
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}



graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "cycling",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
today =datetime(year=2021, month=5, day=12)

post_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "25",

}


# response = requests.post(url=post_endpoint, json=post_params, headers=headers)
# print(response.text)

put_params = {
 "quantity": "2",
}
date_string = today.strftime("%Y%m%d")

put_endpoint = f"{post_endpoint}/{date_string}"

# response = requests.put(url=put_endpoint, json=put_params, headers=headers)
# print(response.text)


response = requests.delete(url=put_endpoint, json=put_params, headers=headers)
print(response.text)
