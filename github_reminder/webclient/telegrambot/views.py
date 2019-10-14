import time
import json
import os, sys
import requests
import datetime
from datetime import timedelta

from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from main.models import accountCode
from .models import messageLogs
from .forms import ConnectTelegramForm
# from settings import TELEGRAM_TOKEN_METROREMINDER, PERSONAL_ID_TELEGRAM


@csrf_exempt
def message_reciever(request):
	try:
		json_message = json.loads(request.body)
	except json.decoder.JSONDecodeError as err:
		return HttpResponse(str(err))
	
	# write the code here to use the following data from JSON Response
	sender_id		= json_message['message']['from'].get('id')
	update_id		= json_message.get('update_id')
	message_text	= json_message['message'].get('text')
	message_date	= json_message['message'].get('date')

	first_name		= json_message['message']['from'].get('first_name')
	last_name		= json_message['message']['from'].get('last_name')

	message_body = ''
	# adding switch case

	if "/start" in message_text:
		''' Command Variation for /start '''
		separate = message_text.split(" ")
		if len(separate) == 1:
			'''its just a command '''
			message_body = '''Welcome
			Please visit [This link to get started](https://septemberthebot.herokuapp.com)'''
			reply_back(message_body, sender_id)
		elif len(separate) >= 2:
			'''its a command, and verification code '''
			# fetch user whos verification code is separate[1]
			print("\t\t separate[1]: {}".format(separate[1]))
			
			verifing_user = accountCode.objects.get(verify_code=separate[1])
			print("\t\t verifing_user: {}".format(verifing_user))
			
			user_verify = verifing_user.user
			print("\t\t user_verify: {}".format(user_verify))


			try:
				'''first run this code'''
				'''connect user's telegram account to account on our db from github'''
				form = ConnectTelegramForm(request.POST or None)
				if form.is_valid():
					print('form is valid')
					message_body = "Something went wrong..."
				else:
					print("Registering user's telegram account...")
					instance = form.save(commit=False)
					instance.user = user_verify		
					# print("\t\t instance.user: {}".format(instance.user))
					# user_verify is the user connected to the verification code
					instance.id_user = sender_id
					# print("\t\t instance.id_user: {}".format(instance.id_user))
					instance.first_name = first_name
					# print("\t\t instance.first_name: {}".format(instance.first_name))
					instance.last_name = last_name
					# print("\t\t instance.last_name: {}".format(instance.last_name))
					# now the instances are created
					instance.save()
					# and they are now saved
					message_body = "This chat is now connected with {}...".format(user_verify)
					# print("message_body: {}".format(message_body))

			except Exception as e:
				'''if something went wrong execute this code'''
				# look for django exception where instance.save() returns if the instance is already saved
				message_body = "Some thing went wrong. Couldn't connect your accounts"
			
			else:
				'''if nothing went wrong, execute this'''
				'''update the user_connected boolean field'''
				user_verify.user_connected = True
				user_verify.save()
			
			finally:
				'''after exception or else, run this code'''
				reply_back(message_body,sender_id)
			
	elif message_text == '/login':
		''' Command Variation for /login '''
		# this should take user to the webpage, where the login process begins
		login_reply()
	else:
		message_body = '''
		Hey.\n
		Please select one of the following messages
		/start - Start the Login process
		/login - Login with Github
		'''
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
