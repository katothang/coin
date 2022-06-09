import json 
import requests

TOKEN = "5399039858:AAGn6Ak5kQfB9QOKGPm63QxFbknF_NXGIHE"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
API_PRICE="https://api.binance.com/api/v1/ticker/price?symbol={}"
API_24H="https://api.binance.com/api/v1/ticker/24hr?symbol={}"
def get_biance_price(coinName):
    coinName = coinName.upper()+'USDT'.upper()
    url = requests.get(API_24H.format(coinName))
    data = url.json()
    if "code" in data:
        return "Mã coin không tồn tại.!"
    return "Giá hiện tại {} Phần trăm thay đổi {}% ".format(data["lastPrice"], data["priceChangePercent"])




