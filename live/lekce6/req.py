import requests

request = requests.get("https://api.golemio.cz/v2/parkings/id", headers={'Authorization': 'access_token myToken'})
print(request)
print(request.text)