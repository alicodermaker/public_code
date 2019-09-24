import telepot
from telepot.loop import MessageLoop

from pprint import pprint
from credentials import user, password, access_token, apex_telegram_bot

bot = telepot.Bot(apex_telegram_bot)
# pprint(bot.getMe())

# response = bot.getUpdates()
# pprint(response)


def handle(msg):
    pprint(msg)

MessageLoop(bot, handle).run_as_thread()
'''
webhook method
https://api.telegram.org/bot969492680:AAHPzYbqnfW_9EP3izkbvh2hzAltq2DllsA/setWebhook?url=https://webhook.site/bb930ac6-5794-422a-8a0e-1e0e0212bc03

getUpdate methodp
https://api.telegram.org/bot969492680:AAHPzYbqnfW_9EP3izkbvh2hzAltq2DllsA/getUpdates

'''