import os
import time

import requests
from dotenv import load_dotenv 
from twilio.rest import Client

load_dotenv()



def get_status(user_id):
    params = {
        'user_ids': user_id,
        'v': 5.92,
        'access_token': os.getenv('ACCESS_TOKEN'),
        'fields': 'online',
    }
    status = requests.post('https://api.vk.com/method/users.get', params=params)
    return status.json()['response'][0].get('online')  # Верните статус пользователя в ВК


def send_sms(sms_text):
    account_sid = "ACb3f3d0a8a0cfad3c6f59b41cec333be6"
    auth_token = "df0a25b80324ee75bf19663b5a15eb44"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                              body= sms_text,
                              from_=os.getenv('NUMBER_FROM'),
                              to=os.getenv('NUMBER_TO')
                          )
    return message.sid  # Верните sid отправленного сообщения из Twilio


if __name__ == '__main__':
    # тут происходит инициализация Client
    vk_id = input('Введите id ')
    while True:
        if get_status(vk_id) == 1:
            send_sms(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
