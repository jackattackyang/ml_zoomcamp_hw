# %%
import requests

# %%
url = 'http://localhost:6969/predict'
client = {"job": "management", "duration": 400, "poutcome": "success"}
response = requests.post(url, json=client).json()
print(response)


