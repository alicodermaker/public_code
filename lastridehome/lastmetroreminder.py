import os, sys
import requests
import datetime
import webbrowser
from datetime import timedelta
import time

import socket

'''
adding the parent directory to PYTHONPATH
'''
# sys.path.insert(0,'..')
sys.path.append(os.path.abspath(os.path.join(os.path.join(os.path.join(os.path.realpath(__file__), '..'), '..'),'..')))

# print(sys.path)
from public_code.credentials import TELEGRAM_TOKEN_METROREMINDER, PERSONAL_ID_TELEGRAM
from public_code.send_telegram_notification import send_message
from public_code.create_log import log_error, log_status

office_ips = [
	'223.230.66.40',
	'183.82.107.34',
]

last_train_time = datetime.time(22, 00, 00)
warning_video = 'https://www.youtube.com/watch?v=CduA0TULnow'

url = 'https://jsonip.com/'

walk_office_to_metro = 5
metro_wait_average = 3
metro_ride_1 = 8
metro_ride_2 = 22
walk_metro_to_home = 20


def is_connected():
	try:
		# connect to the host -- tells us if the host is actually
		# reachable
		socket.create_connection(("www.google.com", 80))
		return True
	except OSError:
		pass
		return False


def main():
	''' Check IP, and take the next step accordingly '''
	current_ip = get_ip()
	if current_ip in office_ips:
		alert_user(current_ip)
	else:
		log_status("Working away from office, with ip address: {}\n".format(current_ip), 'lastmetro')

def log_file(message):
	file_name = '{}/logs/lastmetroreminder_{}.txt'.format(os.path.abspath(os.path.join(os.path.join(os.path.realpath(__file__), '..'),'..')),'{:02d}'.format(datetime.date.today().month))
	# file_name = '{}/logs/lastmetroreminder_{}.txt'.format(os.path.dirname(sys.argv[0]),'{:02d}'.format(datetime.date.today().month))
	with open(file_name,"a+") as f:
		f.write(message)

def get_ip():
	'''Send message after checking, if user is in office'''
	r = requests.get(url)
	response = r.json()
	current_ip = response['ip']
	return current_ip


def alert_user(current_ip):
	''' gather relavent information, and alert user '''
	date_today = datetime.date.today()
	current_time = datetime.datetime.now()
	current_time_str = str('{:%I:%M %p}'.format(current_time.time()))

	log_status("Working in office with ip address: {}\n".format(current_ip), 'lastmetro')
	last_train_in = datetime.datetime.combine(date_today, last_train_time) - datetime.datetime.combine(datetime.date.today(), current_time.time())

	add_minutes = walk_office_to_metro + metro_wait_average + metro_ride_1 + metro_wait_average + metro_ride_2 + walk_metro_to_home
	estimated_arrival = current_time + timedelta(minutes=add_minutes)

	days	= divmod(last_train_in.seconds, 86400)		# Get days
	hours 	= divmod(days[1], 3600)						# Use Reminder of days to calc hours
	minutes	= divmod(hours[1], 60)						# Use Reminder of hours to calc minutes

	time_remaining = "{} hours {} mins".format(hours[0], minutes[0])
	if hours[0] == 0 and minutes[0] < 61:
		webbrowser.open(warning_video)
		notify("Leave now to reach home by {}".format('{:%I:%M %p}'.format(estimated_arrival)), "Last train leaves in {}".format(time_remaining), "ALERT | Last Metro Reminder", 'Hero')
		log_status("Code working fine", 'lastmetro')
	else:	
		notify("Leave now to reach home by {}".format('{:%I:%M %p}'.format(estimated_arrival)), "Last train leaves in {}".format(time_remaining), "Last Metro Reminder", 'Hero')
		log_status("Code working fine", 'lastmetro')

def notify(title, text, subtitle, Audio):
	send_message(title, text, subtitle)
	os.system("""osascript -e 'display notification "{}" with title "{}" subtitle "{}" sound name "{}"'""".format(title, subtitle, text, Audio))

if __name__ == '__main__':
	if is_connected():
		main()
	else:
		log_status("Working with no internet connection", 'lastmetro')
