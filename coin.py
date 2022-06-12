import json 
import requests

TOKEN = "5399039858:AAGn6Ak5kQfB9QOKGPm63QxFbknF_NXGIHE"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
API_PRICE="https://api.binance.com/api/v1/ticker/price?symbol={}"
API_24H="https://api.binance.com/api/v1/ticker/24hr?symbol={}"
LIST_COIN=["BTC", "SHIB", "EOS", "ANC", "EXP","MIR","XEC", "JASMY", "PEOPLE","BTTC","WIN","SPELL","DENT","VTHO","HOT","NBS","MBL","TROY","REEF","KEY","XVG","CKB","SLP"]

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
    coinNamePrint = coinName.upper()
    coinName = coinName.upper()+'USDT'.upper()
    url = requests.get(API_24H.format(coinName))
    data = url.json()
    if "code" in data:
        return ""
    if float(data["priceChangePercent"]) > 10 or float(data["priceChangePercent"]) < -10:
        return "({}) Giá hiện tại {} Phần trăm thay đổi {}% ".format(coinNamePrintdata["lastPrice"], data["priceChangePercent"])
    return ""

def get_list_coin_price(isAuto):
    result = ""
    for coinName in LIST_COIN:
        if isAuto:
            result+= get_biance_price_auto(coinName) + "\n"
        else:
            result+= get_biance_price(coinName) + "\n"
    return result


