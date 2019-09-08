import os
import sys
import csv
import datetime
import requests
import unicodedata
from bs4 import BeautifulSoup

base_url  = 'https://www.apple.com/in/itunes/charts/'

# this code gives the location of script's file
# sys.path[0]
BASE_DIR  = sys.path[0]

def itunes(subfolder):
	platform = "itunes"
	url = base_url + subfolder + "/"
	data = requests.get(url)
	soup = BeautifulSoup(data.text, 'html.parser')

	contents = [s for s in soup.findAll('li', {'class':''})]
	
	app_rank = []
	app_url = []
	app_title = []
	app_genre = []

	for content in contents:
		rank = content.find("strong").text.strip()
		app_rank.append(rank.replace(".", ''))

		url = content.find("a", href=True)['href']
		app_url.append(unicodedata.normalize('NFKD', url).encode('ascii','ignore'))

		title = content.find("h3").text.strip()
		app_title.append(unicodedata.normalize('NFKD', title).encode('ascii','ignore'))

		genre = content.find("h4").text.strip()
		app_genre.append(unicodedata.normalize('NFKD', genre).encode('ascii','ignore'))

	# zip all elements from differnt lists together in a single zip, row
	rows = zip(app_rank, app_title, app_genre, app_url)

	# create or get the file name
	file_name = create_file(platform,subfolder)

	# write the files
	write_file(rows, file_name)

def create_file(platform, file_name):
	'''using the platform name, and current week number, this will create a folder if it doesn't exist'''

	today_datetime = datetime.datetime.now()

	# we need folder_location and folder because it is require to print the file name, and we need to keep it short.
	folder_location = "{}/{}/{}_{}/".format(BASE_DIR, platform, today_datetime.year, (today_datetime.isocalendar()[1]+1))
	folder = "{}/{}_{}/".format(platform, today_datetime.year, today_datetime.isocalendar()[1])
	if not os.path.exists(folder_location):
		os.mkdir(folder_location)
	name = folder + file_name + ".csv"
	return name

def write_file(data, file_name):
	''' using the file name and data, this function will write the data to the file'''
	file_location = "{}/{}".format(BASE_DIR, file_name)
	print("writing file... {}".format(file_name))
	with open(file_location, 'w+') as f:
		writer = csv.writer(f)
		for line in data:
			writer.writerow(line)

def testing(message):
	print(message)

if __name__ == '__main__':
	itunes("free-apps")
	itunes("paid-apps")
