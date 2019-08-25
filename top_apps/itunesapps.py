import os
import csv
import datetime
import requests
import unicodedata
from bs4 import BeautifulSoup

base_url  = 'https://www.apple.com/in/itunes/charts/'

def itunes(platform,subfolder):
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

	rows = zip(app_rank, app_title, app_genre, app_url)
	write_file(rows, create_file(platform,subfolder))


def write_file(data, file_name):
	print("writing file... {}".format(file_name))
	with open(file_name, 'w+') as f:
		writer = csv.writer(f)
		for line in data:
			writer.writerow(line)
		
def create_file(platform, file_name):
	today_datetime = datetime.datetime.now()
	folder = "top_apps/{}_{}/{}/".format(today_datetime.year, today_datetime.isocalendar()[1], platform)
	if not os.path.exists(folder):
		os.mkdir(folder)
	name = folder + file_name + ".csv"
	return name

if __name__ == '__main__':
	itunes('itunes','free-apps')
	itunes("itunes","paid-apps")