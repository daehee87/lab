import sys
import json
import requests
import time
import glob
from datetime import date, datetime

slack_token = sys.argv[1]
channel_id = 'C050MENA4H4'  # general  member id: U054A375LAD
message = 'test'
data = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': slack_token,
        'channel': channel_id,
        'text': message
       }
URL = "https://slack.com/api/chat.postMessage"
res = requests.post(URL, data=data)
print(res.text)


