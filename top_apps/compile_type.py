import os
import sys
import csv
from collections import Counter


BASE_DIR  = sys.path[0]
print(sys.path)
print("----")

''' adding the parent directory to PYTHONPATH '''

sys.path.append(os.path.abspath(os.path.join(os.path.join(os.path.realpath(__file__), '..'), '..')))

print(sys.path)
print("----")
from public_code.send_telegram_notification import send_message

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

	for table in tables:
		for row in table:
			print(row)
		print('\n--')

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

def send_telegram(data):
	pass

if __name__ == '__main__':
	main()