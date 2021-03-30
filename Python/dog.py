import requests, json, string, time
import urllib.request as request
import Message
import Location
import Space
import dog

def RandomDog():
    api_key = "438e05d0-2d33-41d2-8f60-d651b4669990"
    response = requests.get("https://api.thedogapi.com/v1/images/search?"+api_key)
    get_text = response.json()[0]['url']

    access_token = 'Y2VmMGJmZjAtMGM0My00ZTk5LWI2YWYtYjRhMzUxZmY2YmJkOGRiZGM4ZmYtOWYw_PF84_consumer'
    room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vYWRkOWQ2MDAtOTExNC0xMWViLThjNDItNzk3Njc4Y2Q1YmZk'
    url = 'https://webexapis.com/v1/messages'
    headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
    }
    params = {'roomId': room_id, 'file': get_text, 'markdown': "Happy Doggo"}
    requests.post(url, headers=headers, json=params)
