import csv
from collections import Counter


def main():

	get_files()
	'''open csv file and count the row 2 contents'''
	files_location = [
	'/Users/alikhundmiri/Desktop/pythons/alicodermaker/public_code/top_apps/itunes/2019_34/free-apps.csv',
	'/Users/alikhundmiri/Desktop/pythons/alicodermaker/public_code/top_apps/itunes/2019_34/paid-apps.csv',
	]
	
	for location in files_location:
		get_data(location)

def get_files():
	pass

def get_data(location):
	print(location)

	app_catagories = []
	with open(location) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			app_catagories.append(row[2])
	
	count_occurance(app_catagories)

def count_occurance(catagories):
	unique_catagories = Counter(catagories).keys() # equals to list(set(catagories))
	catagories_count = Counter(catagories).values() # counts the elements' frequency
	print(unique_catagories)
	print(catagories_count)

if __name__ == '__main__':
	main()