import sys 
import os
from coin import *
from tele import *

def getPriceCoin():
    last_textchat = (None, None)
    while True:
        try:
            text, chat = get_last_chat_id_and_text(get_updates())
            if (text, chat) != last_textchat:
                send_message(get_biance_price(text), chat)
                last_textchat = (text, chat)
            time.sleep(1)
        except:
            print("abc")
def main():
    getPriceCoin()

if __name__ == '__main__':
    main()