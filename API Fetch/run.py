import requests

url = "www.someurl.com"
auth = None
params = {
   "param_1":"1",
   "param_2":"2"
}
data = {
   "object_1":"x",
   "object_2":"y"
}

response = requests.get(url, auth = auth, params = params, timeout = 3)
if response.status_code == 200:
   response = requests.post(url, data = data, auth = auth)
elif response.status_code == 400:
   print("")
else:
   pass