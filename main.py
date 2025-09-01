import requests

API_KEY = "64e1be288amsh62f12ad6ee39cefp166594jsn8e4c1b6a2e1c"
HOST = "metasyc.p.rapidapi.com"

headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": HOST,
    "Content-Type": "application/json"
}

def connect_mt5(login=123456, password="your_password", server="Broker-Server"):
    url = f"https://{HOST}/connect"
    payload = {
        "login": 52432513,
        "password": "yqE&3Lu8H2qS2yx",
        "server": "ICMARKETSSC-Demo"
    }
    r = requests.post(url, json=payload, headers=headers)
    return r.json()

print(connect_mt5())
