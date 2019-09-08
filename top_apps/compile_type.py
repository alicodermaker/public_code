import os
import sys
import csv
from collections import Counter


BASE_DIR  = sys.path[0]

''' adding the parent directory to PYTHONPATH '''
sys.path.insert(0,'..')

from public_code.create_log import log_error, log_status
from public_code.send_telegram_notification import send_custom_message

# from public_code.send_telegram_notification import send_message

def main():
	get_files()
	'''open csv file and count the row 2 contents'''
	files_location = [
	'/itunes/2019_34/free-apps.csv',
	'/itunes/2019_34/paid-apps.csv',
	]
	
	tables = []
	for location in files_location:
		complete_location = BASE_DIR + location
		data = get_data(complete_location)
		tables.append(data)

	content = zip(files_location, tables)

	for table in content:
		create_message(table)

def get_files():
	pass

def get_data(location):
	app_catagories = []
	with open(location) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			app_catagories.append(row[2])
	
	data = count_occurance(app_catagories)
	return data

def count_occurance(catagories):
	unique_catagories = Counter(catagories).keys() # equals to list(set(catagories))
	catagories_count = Counter(catagories).values() # counts the elements' frequency

	lines = zip(unique_catagories, catagories_count)
	rows = set(lines)
	return rows


def create_message(list_):	
	message = ''' 
*{}*

Application Category - Popularity
'''.format(list_[0].replace("_", "-"))

	for data in list_[1]:
		row_ = ("{} - {} \n".format(data[0], data[1]))
		# print(row_)
		message += row_

	print(message)
	send_custom_message(str(message), "Top App weekly")

def send_telegram(data):
	pass

if __name__ == '__main__':
	main()

'''

[
	{
		('Finance', 4), 
		('Music', 5),
		('Food & Drink', 5), 
		('Photo & Video', 6), 
		('Entertainment', 11), 
		('Utilities', 3), 
		('Games', 19), 
		('Navigation', 1), 
		('Social Networking', 11), 
		('Lifestyle', 4), 
		('Travel', 8), 
		('Shopping', 10), 
		('Reference', 1), 
		('Business', 6), 
		('Productivity', 6)
	}, 
	{
		('Utilities', 4), 
		('Books', 1), 
		('Lifestyle', 1), 
		('Games', 33), 
		('News', 1), 
		('Health & Fitness', 2), 
		('Photo & Video', 24), 
		('Medical', 2), 
		('Education', 5), 
		('Productivity', 9), 
		('Travel', 2), 
		('Social Networking', 2), 
		('Sports', 1), 
		('Entertainment', 2), 
		('Navigation', 1), 
		('Food & Drink', 1), 
		('Music', 5), 
		('Business', 4)
	}
]


'''