import os, sys, re
import time, json, random
import urllib, requests
import threading, traceback, logging
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


logging.basicConfig(filename="botnet.log", level=logging.INFO)
log = logging.getLogger("PhoenixLog")

class Botnet(threading.Thread):

    def __init__(self, token, admin_id, number):

        super().__init__()
        self.token = token
        self.admin_id = admin_id
        self.number = number
        
    def bot_start(self):
        print(f"Bot #{self.number} успешно запущен!")
        threading.Thread(target = time.sleep, args = (999999,)).start()

    def start(self):
        try:
            self.bot_start()
        except Exception as err:
            print(f"Ошибка: {err}")
            time.sleep(1)
            self.start()

    def run(self):
        self.start()
