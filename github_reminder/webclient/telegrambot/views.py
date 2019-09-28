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

	message_body = '''
	Hey, looks like you messages us "{}".\n
	Thank you, but currently Crazy Ex Projects is under development. Please feel free to dm me for more information at [Instagram/AliCoderMaker](https://instagram.com/alicodermaker). Have a great day! 
	'''.format(message_text)

	admin_message = '''
	message from: {}
	message data: {}
	'''.format(sender_id, message_text, settings.PERSONAL_ID_TELEGRAM)
	if str(settings.PERSONAL_ID_TELEGRAM) != str(sender_id):
		# send message to admin
		send_message_admin(admin_message, "Crazy Ex Projects")

	# reply to sender
	send_same_reply(message_body, "Crazy Ex Projects", sender_id)

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
