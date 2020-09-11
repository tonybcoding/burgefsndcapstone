import requests
from test_config import jwt_ep, jwt_cd, jwt_ca, jwt_no
from test_config import movie1, movie2, movie3, actor1, actor2
from test_config import umovie1, umovie2, umovie3, uactor1, uactor2



# add new entries from which to run tests


# show status of each test with each account type


# get request from exec producer
url = "https://burgefsndcapstone.herokuapp.com/actors"
header = {
	"Authorization": f"Bearer {jwt_ep}",
	"Content-Type": "application/json"
}
res = requests.get(url, headers=header)
for entry in res:
	print(entry)


# post/add request from exec producer
url = "https://burgefsndcapstone.herokuapp.com/actors"
header = {
	"Authorization": f"Bearer {jwt_ep}",
	"Content-Type": "application/json"
}
payload = '{"name": "Marion Johnson", "dob": "8/13/1959", "gender": "F"}'
res = requests.post(url, data=payload, headers=header)
for entry in res:
	print(entry)
