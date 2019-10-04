import os, sys, json
import requests
import datetime
import webbrowser
from datetime import timedelta
import time

sys.path.insert(0,'..')

from public_code.credentials import TELEGRAM_TOKEN_METROREMINDER, TELEGRAM_TOKEN_SEPTEMBER, PERSONAL_ID_TELEGRAM

def custom_bot_admin(message_body, from_, to_):
	''' Send message to on telegram '''
	text_message = '''
	{}
	_message from {}_
	'''.format(message_body, from_)
	url  = 'https://api.telegram.org/bot{}/sendMessage'.format(to_)
	payload = {'text': text_message, 'chat_id':PERSONAL_ID_TELEGRAM, 'parse_mode':'Markdown'}
	r = requests.post(url, data=payload)

def send_custom_message(message_body, from_):
	''' Send message to on telegram '''
	text_message = '''
	{}
	_message from {}_
	'''.format(message_body, from_)
	url  = 'https://api.telegram.org/bot{}/sendMessage'.format(TELEGRAM_TOKEN_METROREMINDER)
	payload = {'text': text_message, 'chat_id':PERSONAL_ID_TELEGRAM, 'parse_mode':'Markdown'}
	r = requests.post(url, data=payload)


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
	'''
	print(r.status_code)
	if r.status_code == 200:
		print("Message sent!")
	else:
		print("some error!")
	print(r.text)
	'''

def send_message_simple(title, text):
	''' Send message to on telegram '''
	text_message = '''
		*{}*
		{}
	'''.format(title, text)
	url  = 'https://api.telegram.org/bot{}/sendMessage'.format(TELEGRAM_TOKEN_METROREMINDER)
	# payload = {'text': text_message, 'chat_id':PERSONAL_ID_TELEGRAM, 'parse_mode':'Markdown'}
	reply_markup={
		"keyboard":
		[
			[
			{"text" : "Login via Github", 'url' : "https://www.instagram.com/alicodermaker"},
			],
			[
			{"text" : "Explain How it works", 'url' : "https://septemberthebot.herokuapp.com"},
			]
		],
		"one_time_keyboard" : True
	}

	payload = {
		'text': text_message,
		'chat_id':PERSONAL_ID_TELEGRAM,
		'parse_mode':'Markdown',
		'reply_markup' : json.dumps(reply_markup)
	}
	r = requests.post(url, data=payload)
	print(r.text)

if __name__ == '__main__':
	message_body = """
		Welcome user,
		

		To proceed with the app, 
		select "Login in with Github"


		To learn how it works, 
		select "Explain How it works"
	
	Please Choose an option to continue...
	"""

	send_message_simple("Crazy Ex Projects", message_body)