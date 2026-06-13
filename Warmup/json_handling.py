import json

data = {
    "name":"Bharath",
    "role":"SRE"
}


json_data = json.dumps(data)
print(json_data)

parsed_data = json.loads(json_data)
print(parsed_data)

#Working with APIS

import requests

response = requests.get("https://www.google.com")
print(response.status_code)
#print(response.headers)

# POST request
# requests.post(
#     url,
#     json={"name":"Bharath"}
# )

# Environment variables
#bash
#export GITHUB_TOKEN=123

#python
# import os
# os.getenv("GITHUB_TOKEN")

#date and time
from datetime import datetime
print(datetime.now())

date = datetime.now()
datetime_string = date.strftime("%Y-%m-%d")

print(datetime_string)

#logging
import logging
logging.basicConfig(level=logging.DEBUG)

logging.info("This is a info message")
logging.debug("This is a debug message")

#Regular expression
import re

msg = "I got 92% in my last exam"
percentage = re.findall(r'\d+%',msg)
print(percentage)