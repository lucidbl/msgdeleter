import requests
import time

token = input("Your token: ")
channel_id = input("Channel ID: ")
tokenz = {"authorization":f"{token}"}

while True:
    req = requests.get(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers = tokenz)
    penis = req.json()
    def obrisi(message_id):
        brisi = requests.delete(f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}", headers = tokenz)
        print(brisi)
    
    for id in penis:
        obrisi(id['id'])
        time.sleep(1)
