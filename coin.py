import json 
import requests
from Constaint import *
TOKEN = "5399039858:AAGn6Ak5kQfB9QOKGPm63QxFbknF_NXGIHE"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
API_PRICE="https://api.binance.com/api/v1/ticker/price?symbol={}"
API_24H="https://api.binance.com/api/v1/ticker/24hr?symbol={}"

def get_biance_price(coinName):
    if coinName.upper() == 'LIST':
        return get_list_coin_price(False)
    coinNamePrint = coinName.upper()
    coinName = coinName.upper()+'USDT'.upper()
    url = requests.get(API_24H.format(coinName))
    data = url.json()
    if "code" in data:
        return "Mã coin không tồn tại.!"
    return "({}) Giá hiện tại {} Phần trăm thay đổi {}% ".format(coinNamePrint,data["lastPrice"], data["priceChangePercent"])

def get_biance_price_auto(coinName):
    Constaint.LIST_FAVOURITE  = list(dict.fromkeys(Constaint.LIST_FAVOURITE))
    coinNamePrint = coinName.upper()
    coinName = coinName.upper()+'USDT'.upper()
    url = requests.get(API_24H.format(coinName))
    data = url.json()
    if "code" in data:
        return ""
    if float(data["priceChangePercent"]) > Constaint.RATE_UP or float(data["priceChangePercent"]) < Constaint.RATE_DOWN:
        return "({}) Giá hiện tại {} Phần trăm thay đổi {}% ".format(coinNamePrint,data["lastPrice"], data["priceChangePercent"])
    return ""

def get_list_coin_price(isAuto):
    list_coin = Constaint.LIST_COIN
    if isAuto:
       list_coin= Constaint.LIST_FAVOURITE 
    result = ""
    for coinName in list_coin:
        if isAuto:
            result+= get_biance_price_auto(coinName) + "\n"
        else:
            result+= get_biance_price(coinName) + "\n"
    return result


