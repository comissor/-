# -*- coding: utf-8 -*-
from botnet import Botnet
import traceback, time

ADMIN_ID = "Ваш айди"

def create_bots():
    
    with open("accounts.txt") as f:
        accounts = f.readlines()
        
    for token in accounts:
        
        try:
                            
            Botnet(token = token, admin_id = ADMIN_ID, number = accounts.index(token)).start()
            time.sleep(0.5)
        
        except Exception as error:
            print(f"Не удалось запустить бота: {traceback.format_exc()}")

if __name__ == "__main__":
    create_bots()
    print("Ботнет в полной боевой готовности!")
    