import requests

API_KEY = "your-rapid-api-key"
HOST = "metasyc.p.rapidapi.com"

headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": HOST,
    "Content-Type": "application/json"
}

def connect_mt5(login=123456, password="your_password", server="Broker-Server"):
    url = f"https://{HOST}/connect"
    payload = {
        "login": "mt5_login",
        "password": "mt5_password",
        "server": "your_broker_server"
    }
    r = requests.post(url, json=payload, headers=headers)
    return r.json()

print(connect_mt5())
