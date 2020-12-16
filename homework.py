import os
import time

import requests
from dotenv import load_dotenv 
from twilio.rest import Client

load_dotenv()



def get_status(user_id):
    params = {"user_ids": user_id,
              "v": 5.92,
              "fields": "online",
              "access_token": os.getenv('ACCESS_TOKEN')
              }

    response = requests.post(url='https://api.vk.com/method/users.get',
                             data=params).json()['response']
    status = response[0].get("online")
    return status



def sms_sender(sms_text):

    account_sid = "ACb3f3d0a8a0cfad3c6f59b41cec333be6"
    auth_token = "df0a25b80324ee75bf19663b5a15eb44"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                              body= sms_text,
                              from_=os.getenv('NUMBER_FROM'),
                              to=os.getenv('NUMBER_TO')
                          )
    return message.sid  

if __name__ == '__main__':
    vk_id = input('Введите id ')
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)

#небольшой комментарий: в заготовке функция send_sms получала два аргумента, но тесты потребовали
#её переименовать, а также сделать, чтобы она получала один аргумент,
#поэтому клиент не там, где было отмечено,
#иначе не проходят тесты