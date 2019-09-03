import os, sys
import requests
import datetime
import webbrowser
from datetime import timedelta
import time

from credentials import TELEGRAM_TOKEN_METROREMINDER, PERSONAL_ID_TELEGRAM



def send_message(title, text, subtitle):
	''' Send message to on telegram '''
	text_message = '''
		*{}*
		{}
		_{}_
	'''.format(subtitle, text, title)
	url  = 'https://api.telegram.org/bot{}/sendMessage'.format(TELEGRAM_TOKEN_METROREMINDER)
	payload = {'text': text_message, 'chat_id':PERSONAL_ID_TELEGRAM, 'parse_mode':'Markdown'}
	r = requests.post(url, data=payload)

if __name__ == '__main__':
	message_body = """

		* * *
		This bot can be used by any script... check [Github](https://github.com/alicodermaker/public_code/blob/master/send_telegram_notification.py)
	"""

	send_message("by ali khundmiri's bot...", message_body, "Ali's Telegram Bot")