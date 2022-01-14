import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events

api_id = '13944982'
api_hash = '0947f1da826caa937c5ccb1cbafb9264'
client = TelegramClient('session', api_id, api_hash)
client.connect()
response = client.invoke(ResolveUsernameRequest("harrymcmoney"))
print(response.chats[0].access_hash)
client.disconnect()
