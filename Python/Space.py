import requests
import json

#Y2VmMGJmZjAtMGM0My00ZTk5LWI2YWYtYjRhMzUxZmY2YmJkOGRiZGM4ZmYtOWYw_PF84_consumer

#"Y2lzY29zcGFyazovL3VzL1JPT00vYWRkOWQ2MDAtOTExNC0xMWViLThjNDItNzk3Njc4Y2Q1YmZk

def Space():
    response = requests.get(" https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
    get_text = response.json()["explanation"]
    access_token = 'Y2VmMGJmZjAtMGM0My00ZTk5LWI2YWYtYjRhMzUxZmY2YmJkOGRiZGM4ZmYtOWYw_PF84_consumer'
    room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vYWRkOWQ2MDAtOTExNC0xMWViLThjNDItNzk3Njc4Y2Q1YmZk'
    url = 'https://webexapis.com/v1/messages'
    headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
    }
    params = {'roomId': room_id, 'markdown': get_text}
    requests.post(url, headers=headers, json=params)
