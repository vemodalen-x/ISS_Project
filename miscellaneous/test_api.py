

import json
import base64
import requests
"""
send requests
"""


# image filepath jpg/png/bmp foramte
IMAGE_FILEPATH = r"C:\Users\vemodalen\Desktop\ISS_PROJECT\NFL_dataset\Images\57502_000480_Endzone_frame0495.jpg"

# threshold of output confidence
PARAMS = {"threshold": 0.3}

# api url
MODEL_API_URL = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/detection/helmet_detecion"

ACCESS_TOKEN = ""
API_KEY = "c72mY1qBgLcGeCp3gZRbnw0R"
SECRET_KEY = "5P4E2HTjCMWR9Thj6pDe5eFwU3ITRdhp"


print("1. read image '{}'".format(IMAGE_FILEPATH))
with open(IMAGE_FILEPATH, 'rb') as f:
    base64_data = base64.b64encode(f.read())
    base64_str = base64_data.decode('UTF8')
print("file in PARAMS with base64 code")
PARAMS["image"] = base64_str


if not ACCESS_TOKEN:
    print("2. ACCESS_TOKEN is none get token")
    auth_url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials"               "&client_id={}&client_secret={}".format(API_KEY, SECRET_KEY)
    auth_resp = requests.get(auth_url)
    auth_resp_json = auth_resp.json()
    ACCESS_TOKEN = auth_resp_json["access_token"]
    print("new ACCESS_TOKEN: {}".format(ACCESS_TOKEN))
else:
    print("2. access existed ACCESS_TOKEN")


print("3. send 'MODEL_API_URL' request")
request_url = "{}?access_token={}".format(MODEL_API_URL, ACCESS_TOKEN)
response = requests.post(url=request_url, json=PARAMS)
response_json = response.json()
response_str = json.dumps(response_json, indent=4, ensure_ascii=False)
print("results:{}".format(response_str))