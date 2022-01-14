""" Functions related to the Telegram bot """
from logging.handlers import RotatingFileHandler
import telegram_send
import sys
import logging
from os import environ
import requests
from dotenv import load_dotenv
from utils import exception_info


# importing all required libraries
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events

logging.basicConfig(handlers=[RotatingFileHandler('data/log.txt', maxBytes=524288, backupCount=10)],
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

load_dotenv('config.cfg')
BOT_TOKEN = environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = environ.get('TELEGRAM_CHAT_ID')

# get your api_id, api_hash, token
# from telegram as described above
api_id = '13944982'
api_hash = '0947f1da826caa937c5ccb1cbafb9264'
token = BOT_TOKEN

# your phone number
phone = '15103201791'

# creating a telegram session and assigning
# it to a variable client
client = TelegramClient('session', api_id, api_hash)

# connecting and building the session
client.connect()

# in case of script ran first time it will
# ask either to input token or otp sent to
# number or sent or your telegram id
if not client.is_user_authorized():

    client.send_code_request(phone)

    # signing in the client
    client.sign_in(phone, input('Enter the code: '))


def telegram_bot_sendtext(bot_message):
    """
        Function to send text messages to a telegram bot
    Args:
        bot_message (str): message you want to send to the bot
    """
    # url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=HTML&text={bot_message}"
    # # telegram_send.send(messages=[bot_message])
    # print(url)
    # try:
    #     response = requests.get(url).json()
    #     LOGGER.info(f"Telegram message status: {response['ok']}")
    #     print(response)
    # except requests.exceptions.RequestException:
    #     print("error")
    #     LOGGER.error(exception_info(sys.exc_info()))
    #     sys.exit(1)
    try:
        # receiver user_id and access_hash, use
        # my user_id and access_hash for reference
        # receiver = InputPeerUser('1788435379', 0)
        # receiver = client.get_entity('1788435379')
        #
        # # sending message using telegram client
        # client.send_message(receiver, bot_message, parse_mode='html')
        entity = client.get_entity('harrymcmoney')
        client.send_message(1788435379, bot_message)
    except Exception as e:

        # there may be many error coming in while like peer
        # error, wrong access_hash, flood_error, etc
        print(e);
