import requests, json, string, time
import urllib.request as request
import Message
import Location
import Space
import dog

# Personal acess token = Y2VmMGJmZjAtMGM0My00ZTk5LWI2YWYtYjRhMzUxZmY2YmJkOGRiZGM4ZmYtOWYw_PF84_consumer
access_token = 'Y2VmMGJmZjAtMGM0My00ZTk5LWI2YWYtYjRhMzUxZmY2YmJkOGRiZGM4ZmYtOWYw_PF84_consumer'
# Room Webex Team
room_id = { 0: ["Hello_test", "Y2lzY29zcGFyazovL3VzL1JPT00vYWRkOWQ2MDAtOTExNC0xMWViLThjNDItNzk3Njc4Y2Q1YmZk"],
            1: ["NPA2020@ITKMITL", "Y2lzY29zcGF0yazovL3VzL1JPT00vNjA5Nzk5NDAtNTU3My0xMWViLWEzNzUtY2JkMGE4ZjAxYTA3"]}
print("Please select your room :\n\t[0] : Webex space for hello_test\n\t[1] : NPA2020@ITKMITL")
room_id = room_id[int(input("Select your room : "))]

while True:
    text = Message.GetMessage(access_token, room_id)
    if text == "None":
        continue
    # Location Mode0
    elif text.lower() == "location":
        print(".........................................Location")
        url = 'https://webexapis.com/v1/messages'
        headers = {
            'Authorization': 'Bearer {}'.format(access_token),
            'Content-Type': 'application/json'
        }
        params = {'roomId': room_id[1], 'markdown': "Please Enter Location..."}
        requests.post(url, headers=headers, json=params)
        Location.CheckText(text, access_token, room_id)
    # DOG Stack Mode
    elif text.lower() == "randog":
        url = 'https://webexapis.com/v1/messages'
        headers = {
            'Authorization': 'Bearer {}'.format(access_token),
            'Content-Type': 'application/json'
        }
        params = {'roomId': room_id[1], 'markdown': "Let's see Dog picture..."}
        requests.post(url, headers=headers, json=params)
        dog.RandomDog()
        print("Doggo Let's Go")
    # Space Mode
    elif text.lower() == "space":
        url = 'https://webexapis.com/v1/messages'
        headers = {
            'Authorization': 'Bearer {}'.format(access_token),
            'Content-Type': 'application/json'
        }
        params = {'roomId': room_id[1], 'markdown': "Space Quote..."}
        requests.post(url, headers=headers, json=params)
        Space.Space()
        print("Space Quote is gone...")
    time.sleep(5)
