import time
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

	sender_object = User.objects.filter(user_id__exact=sender_id).get()

	update_id     = json_message.get('update_id')

	message_text  = json_message['message'].get('text')

	message_date  = json_message['message'].get('date')

	send_custom_message(message_text, "Ali's Automated reply")

	return HttpResponse('OK')

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

When in stage 2, save messages in our database as user 'anonymous'


def get_telegram_update(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('newsletter:index'))
	else:
		# pass
		return HttpResponseRedirect(reverse('accounts:profile'))

	context = {
		'production' : settings.PRODUCTION,
	}
	return render(request, 'accounts/profile.html', context)


def index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('newsletter:index'))
	else:
		# pass
		return HttpResponseRedirect(reverse('accounts:profile'))

	context = {
		'production' : settings.PRODUCTION,
	}
	return render(request, 'accounts/profile.html', context)
--------------------------------------------------------------------------------------------
'''


def custom_bot_admin(message_body, from_, to_):
	''' Send message to on telegram '''
	text_message = '''
	{}
	_message from {}_
	'''.format(message_body, from_)
	url  = 'https://api.telegram.org/bot{}/sendMessage'.format(to_)
	payload = {'text': text_message, 'chat_id':settings.PERSONAL_ID_TELEGRAM, 'parse_mode':'Markdown'}
	r = requests.post(url, data=payload)

def send_custom_message(message_body, from_):
	''' Send message to on telegram '''
	text_message = '''
	{}
	_message from {}_
	'''.format(message_body, from_)
	url  = 'https://api.telegram.org/bot{}/sendMessage'.format(settings.TELEGRAM_TOKEN_SEPTEMBER)
	payload = {'text': text_message, 'chat_id':settings.PERSONAL_ID_TELEGRAM, 'parse_mode':'Markdown'}
	r = requests.post(url, data=payload)


def send_message(title, text, subtitle):
	''' Send message to on telegram '''
	text_message = '''
		*{}*
		{}
		_{}_
	'''.format(subtitle, text, title)
	url  = 'https://api.telegram.org/bot{}/sendMessage'.format(settings.TELEGRAM_TOKEN_SEPTEMBER)
	payload = {'text': text_message, 'chat_id':settings.PERSONAL_ID_TELEGRAM, 'parse_mode':'Markdown'}
	r = requests.post(url, data=payload)
	'''
	print(r.status_code)
	if r.status_code == 200:
		print("Message sent!")
	else:
		print("some error!")
	print(r.text)
	'''
if __name__ == '__main__':
	message_body = """
		we are working on some testing. please be patient..
		
		This bot can be used by any script... check [Github page for code](https://github.com/alicodermaker/public_code/blob/master/send_telegram_notification.py)
	"""

	send_message("Black is better than yellow...", message_body, "Ali's Telegram Bot")