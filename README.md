# 🚀 MetaSync Python Tutorial – Connect MetaTrader 5 via RapidAPI

MetaSync is a **universal API bridge** that allows you to connect **MetaTrader 4/5 (MT4/MT5)** with **Python, JavaScript, and any external app** without writing MQL.  
This tutorial shows you how to **authenticate and connect to your MT5 account** using Python and the MetaSync API hosted on RapidAPI.  

---

## 🎥 Video Tutorial  

[![Watch the video](https://img.youtube.com/vi/mj7Y1D__sCI/0.jpg)](https://www.youtube.com/watch?v=mj7Y1D__sCI&t=7s)


## 📦 Requirements

- Python 3.7+ installed
- `requests` library (`pip install requests`)
- A **RapidAPI account** (free to start)
- Subscribed to the **MetaSync API** on RapidAPI  
  👉 [MetaSync API on RapidAPI](https://rapidapi.com/api4meta/api/metasync)  
- MetaTrader 5 terminal installed and logged into a **broker account** (demo or live)

---

## 🔑 Setup

1. **Get your RapidAPI Key**  
   - Sign in to [RapidAPI]([https://rapidapi.com](https://rapidapi.com/metasync-metasync-default/api/metasyc))  
   - Go to **My Apps > Security**  
   - Copy your **X-RapidAPI-Key**

2. **Configure your credentials**  
   Update the script with:
   - `API_KEY` → Your RapidAPI key  
   - `login` → Your MT5 account login number  
   - `password` → Your MT5 account password  
   - `server` → Your broker server name (e.g., *MetaQuotes-Demo*)  

---

## 🐍 Example Python Script

```python
import requests

# Your RapidAPI credentials
API_KEY = "your-rapid-api-key"
HOST = "metasyc.p.rapidapi.com"

# Headers for authentication
headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": HOST,
    "Content-Type": "application/json"
}
```
# Function to connect to MT5

```python
def connect_mt5(login=123456, password="your_password", server="Broker-Server"):
    url = f"https://{HOST}/connect"
    payload = {
        "login": login,
        "password": password,
        "server": server
    }
    r = requests.post(url, json=payload, headers=headers)
    return r.json()

# Test the connection
print(connect_mt5(
    login=1234567, 
    password="your_mt5_password", 
    server="MetaQuotes-Demo"
))
````

---

## 🖥️ How It Works

* The script sends a **POST request** to the `/connect` endpoint of the MetaSync API.
* MetaSync then establishes a session between your code and the running **MT5 terminal**.
* If successful, the response will include a **connection confirmation** with details like account login and server.

---

## ✅ Sample Response

```json
{
  "status": "connected",
  "account": {
    "login": 1234567,
    "server": "MetaQuotes-Demo",
    "name": "Demo Account"
  }
}
```

---

## 📌 Notes

* Always keep your **API key** and MT5 credentials private.
* The terminal must be **open and logged in** for the connection to work.
* For testing, use a **demo account** before trying on a live account.

---

## 🤝 Support

If you encounter issues:

* Confirm your MT5 terminal is running and connected.
* Double-check your login, password, and broker server name.
* Leave feedback or questions via the RapidAPI portal or community.

---

### 🎯 You’ve now connected MetaTrader 5 to Python using MetaSync!



