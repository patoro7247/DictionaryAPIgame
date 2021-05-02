
import requests
import pprint
import json


#store the request in this r variable
url = "https://lingua-robot.p.rapidapi.com/language/v1/entries/en/respect"

headers = {
    'x-rapidapi-key': "5da15bccffmsh6b27a6ff8f3b2f8p152169jsn23a9f2be1883",
    'x-rapidapi-host': "lingua-robot.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

#pprint.pprint(response.json()['entries'][0]['lexemes'][0]['antonymSets'][0])

data = json.load(response.json())

print(data['entries'])
