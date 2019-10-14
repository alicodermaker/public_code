from .models import accountCode

from telegrambot.models import telegramAccount, messageLogs, Message

''' This file contains code to send weekly messages'''

def function():
	'''main control panel'''
	get_users()
	scan_github()
	

def get_users():
	'''get a list of users who have cpmpleted registration. 
	i.e. signed up on github and we have their telegram'''
	pass

def scan_github():
	''' scan a single user's github '''
	pass




if __name__ == '__main__':
	function()