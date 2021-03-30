import requests, json, string, time
import urllib.request as request
import Message
import Location
import Space
import dog

def GetMessage(access_token, room_id):
    """ Get message from WebEx """
    url = 'https://webexapis.com/v1/messages?roomId={}'.format(room_id[1])
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
    }
    res = requests.get(url, headers=headers)
    text = res.json()["items"][0]["text"]

    if text[0] == '/':
        return text[1:]
    else:
        return "None"