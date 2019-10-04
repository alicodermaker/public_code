import time
import json
import os, sys
import requests
import datetime
from datetime import timedelta

from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import messageLogs

# from settings import TELEGRAM_TOKEN_METROREMINDER, PERSONAL_ID_TELEGRAM


@csrf_exempt
def message_reciever(request):
	try:
		json_message = json.loads(request.body)
	except json.decoder.JSONDecodeError as err:
		return HttpResponse(str(err))
	
	# write the code here to use the following data from JSON Response
	sender_id     = json_message['message']['from'].get('id')
	update_id     = json_message.get('update_id')
	message_text  = json_message['message'].get('text')
	message_date  = json_message['message'].get('date')

	message_body = ''
	# adding switch case
	if "/start" in message_text:
		separate = message_text.split(" ")
		try:
			separate[1]
			# separate[1] is the verification string
			
			message_body = '''
			"{}"
			'''.format(separate[1])
			reply_back(message_body,sender_id)				

		except:
			# this message_text does not contains verification string
			message_body = '''Welcome
			Please visit [This link to get started](https://septemberthebot.herokuapp.com)'''
			reply_back(message_body, sender_id)
	
	elif message_text == '/login':
		login_reply()
	else:
		message_body = '''
		Hey, looks like you messages us "{}".\n
		Please select one of the following messages

		/start - Start the Login process
		/login - Login with Github
		'''.format(message_text)
		reply_back(message_body, sender_id)

	admin_message = '''
	message from: {}
	message data: {}
	'''.format(sender_id, message_text, settings.PERSONAL_ID_TELEGRAM)

	if str(settings.PERSONAL_ID_TELEGRAM) != str(sender_id):
		# send message to admin
		send_message_admin(admin_message, "Crazy Ex Projects")

	return HttpResponse('OK')

def send_message_admin(message_body, from_):
	''' Send message to on telegram '''
	text_message = '''
	{}
	_message from {}_
	'''.format(message_body, from_)
	url  = 'https://api.telegram.org/bot{}/sendMessage'.format(settings.TELEGRAM_TOKEN_SEPTEMBER)
	payload = {'text': text_message, 'chat_id':settings.PERSONAL_ID_TELEGRAM, 'parse_mode':'Markdown'}
	r = requests.post(url, data=payload)


def login_reply():
	''' Send  to login via github '''
	text_message = '''{}'''.format("Please click on the 'Login Via Github' button")
	url  = 'https://api.telegram.org/bot{}/sendMessage'.format(settings.TELEGRAM_TOKEN_SEPTEMBER)
	
	reply_markup={
		"inline_keyboard":
		[
			[
			{"text" : "Login via Github", 'url' : "https://septemberthebot.herokuapp.com/oauth/login/github/"},
			],
			[
			{"text" : "Learn how it works", 'url' : "https://septemberthebot.herokuapp.com"},
			]
		],
	}

	payload = {
		'text': text_message,
		'chat_id':settings.PERSONAL_ID_TELEGRAM,
		'parse_mode':'Markdown',
		'reply_markup' : json.dumps(reply_markup)
	}
	r = requests.post(url, data=payload)



def reply_back(message_body, to_):
	''' Send message to on telegram '''
	text_message = '''{}'''.format(message_body)
	url  = 'https://api.telegram.org/bot{}/sendMessage'.format(settings.TELEGRAM_TOKEN_SEPTEMBER)
	payload = {'text': text_message, 'chat_id':to_, 'parse_mode':'Markdown'}
	r = requests.post(url, data=payload)


def reply_back_inline_keyboard(message_body, to_):
	''' Send message to on telegram '''
	text_message = '''{}'''.format(message_body)
	url  = 'https://api.telegram.org/bot{}/sendMessage'.format(settings.TELEGRAM_TOKEN_SEPTEMBER)
	payload = {'text': text_message, 'chat_id':to_, 'parse_mode':'Markdown'}
	r = requests.post(url, data=payload)


def send_same_reply(message_body, from_, to_):
	''' Send message to on telegram '''
	text_message = '''
	{}
	_message from {}_
	'''.format(message_body, from_)
	url  = 'https://api.telegram.org/bot{}/sendMessage'.format(settings.TELEGRAM_TOKEN_SEPTEMBER)
	payload = {'text': text_message, 'chat_id':to_, 'parse_mode':'Markdown'}
	r = requests.post(url, data=payload)


'''
	USER FLOW

	TELEGRAM > WEBSITE > GITHUB

	1. Find the bot on telegram.
	2. message bot, /start
	3. bot takes through a few steps
		1. login via github
			* this creates a new account on our website, and the user's telegram info is stored.
		2.(later) change password
	4. active customer
'''
