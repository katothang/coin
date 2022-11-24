import sys 
import os
from coin import *
from Constaint import *
from tele import *
from threading import Thread


def getPriceCoin():
    while True:
        try:
            text, chat = get_last_chat_id_and_text(get_updates())
            if (text, chat) != Constaint.LAST_CHAT:
                if configData(text,chat):
                    continue
            if (text, chat) != Constaint.LAST_CHAT and len(text) < 10:
                send_message(get_biance_price(text), chat)
                Constaint.LAST_CHAT = (text, chat)
            time.sleep(0.5)
        except Exception as e:
            print(e)
def getPriceCoinAuto():
    while True:
        result = get_list_coin_price(True)
        if(result != ""):
            send_message(result, Constaint.CHAT_ID)
        time.sleep(Constaint.TIME_AUTO)

def configData(text,chat):
    if text.upper() == "DSYT": #lệnh xem danh sách yêu thích
        send_message("\n".join(str(x) for x in Constaint.LIST_FAVOURITE), chat)
        Constaint.LAST_CHAT = (text, chat)
        return True
    elif "ADD" in text.upper(): # thêm đồng coin vào danh sách yêu thích
        coinName = text.upper().split(" ")[1].strip()
        if coinName in Constaint.LIST_FAVOURITE:
            send_message("Đồng coin {} đã tồn tại".format(coinName), chat)
            Constaint.LAST_CHAT = (text, chat)
            return True
        Constaint.LIST_FAVOURITE.append(coinName)
        send_message("Thêm thành công coin {}".format(coinName), chat)
        Constaint.LAST_CHAT = (text, chat)
        return True
    elif "REMOVE" == text.upper().split(" ")[0].strip(): #Xóa đồng coin khỏi danh sách theo dõi
        coinName = text.upper().split(" ")[1].strip()
        Constaint.LIST_FAVOURITE.remove(coinName)
        send_message("Xóa thành công coin {}".format(coinName), chat)
        Constaint.LAST_CHAT = (text, chat)
        return True
    elif "RATE_UP" in text.upper(): # set thông báo nếu đồng coin trong danh sách tăng theo % (vd RATE_UP 10 thì khi đồng coin tăng 10% sẽ báo về bot)
        rate = text.upper().split(" ")[1]
        Constaint.RATE_UP = float(rate.strip())
        send_message("setting rate up = {}".format(Constaint.RATE_UP), chat)
        Constaint.LAST_CHAT = (text, chat)
        return True
    elif "RATE_DOWN" in text.upper(): # Tương tự set thông số % giảm của đồng coin
        rate = text.upper().split(" ")[1]
        Constaint.RATE_DOWN = float(rate.strip())
        send_message("setting rate down = {}".format(Constaint.RATE_DOWN), chat)
        Constaint.LAST_CHAT = (text, chat)
        return True
    elif "AUTO" == text.upper().split(" ")[0]: # thời gian quét giá đồng coin vd 10 giây 1 lần quét
        rate = text.upper().split(" ")[1]
        Constaint.TIME_AUTO = int(rate.strip())
        send_message("setting time auto = {} giây".format(Constaint.TIME_AUTO), chat)
        Constaint.LAST_CHAT = (text, chat)
        return True
    elif "AUTOALL" in text.upper(): # Theo dõi tất cả các đồng coin được chỉ định trong Constaint.py
        Constaint.LIST_FAVOURITE+=Constaint.LIST_COIN
        send_message("Theo dõi all list thành công.!", chat)
        Constaint.LAST_CHAT = (text, chat)
        return True
    elif "REMOVEALL" in text.upper(): #Xóa tất cả danh sách theo dõi
        Constaint.LIST_FAVOURITE = []
        send_message("Xóa theo dõi thành công.!", chat)
        Constaint.LAST_CHAT = (text, chat)
        return True
    elif text.upper() == "CONFIG": #Xem tất cả các config
        view_setting = "List coin yêu thích: {} \n RATE_UP = {}, RATE_DOWN = {} \n TIME_AUTO: {} giây".format("\n".join(str(x) for x in Constaint.LIST_FAVOURITE), Constaint.RATE_UP, Constaint.RATE_DOWN, Constaint.TIME_AUTO)
        send_message(view_setting, chat)
        Constaint.LAST_CHAT = (text, chat)
        return True
    else:
        return False


def main():
    Constaint.LAST_CHAT = (None, None)
    Thread(target = getPriceCoinAuto).start()
    Thread(target = getPriceCoin).start()

    
if __name__ == '__main__':
    main()