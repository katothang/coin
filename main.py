import sys 
import os
from coin import *
from tele import *
from threading import Thread

def getPriceCoin():
    last_textchat = (None, None)
    while True:
        try:
            text, chat = get_last_chat_id_and_text(get_updates()).''
            if (text, chat) != last_textchat and len(text) < 10:
                send_message(get_biance_price(text), chat)
                last_textchat = (text, chat)
            time.sleep(0.5)
        except:
            print("abc")
def getPriceCoinAuto():
    while True:
        result = get_list_coin_price(True)
        if(result != ""):
            send_message(result, "1625452249")
        time.sleep(600)

def main():
    Thread(target = getPriceCoinAuto).start()
    Thread(target = getPriceCoin).start()

    
if __name__ == '__main__':
    main()