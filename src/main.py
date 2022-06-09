import sys 
import os
import sched
sys.path.append(os.path.abspath("src/"))
from coin import *
from tele import *

def main():
    last_textchat = (None, None)
    while True:
        text, chat = get_last_chat_id_and_text(get_updates())
        if (text, chat) != last_textchat:
            send_message(get_biance_price(text), chat)
            last_textchat = (text, chat)
        time.sleep(1)

if __name__ == '__main__':
    main()

