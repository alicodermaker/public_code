import wget
import urllib.parse

from bs4 import BeautifulSoup
from urllib.request import urlopen

import re

def main():
	# print('Beginning file download with wget module')

	url = 'http://51.15.61.24/Gravity%20Falls/Episodes/'


	html_page = urlopen(url)
	soup = BeautifulSoup(html_page, features="lxml")
	for link in soup.find_all('a'):
		print(link.get('href'))


	# wget.download(url, '/Users/alikhundmiri/Desktop/Entertainment/TV')
	pass

def download():
	list_ = [
	"http://51.15.61.24/Gravity%20Falls/Episodes/Gravity%20Falls%20-%20S01E08%20-%20Irrational%20Treasure.mp4",
	"http://51.15.61.24/Gravity%20Falls/Episodes/Gravity%20Falls%20-%20S01E09%20-%20The%20Time%20Traveler's%20Pig.mp4",
	"http://51.15.61.24/Gravity%20Falls/Episodes/Gravity%20Falls%20-%20S01E10%20-%20Fight%20Fighters.mp4",
	"http://51.15.61.24/Gravity%20Falls/Episodes/Gravity%20Falls%20-%20S01E11%20-%20Little%20Dipper.mp4",
	"http://51.15.61.24/Gravity%20Falls/Episodes/Gravity%20Falls%20-%20S01E12%20-%20Summerween.mp4",
	"http://51.15.61.24/Gravity%20Falls/Episodes/Gravity%20Falls%20-%20S01E13%20-%20Boss%20Mabel.mp4",
	"http://51.15.61.24/Gravity%20Falls/Episodes/Gravity%20Falls%20-%20S01E14%20-%20Bottomless%20Pit.mp4"

	]
	for url in list_:
		print("found 51.15.61.24/Gravity%20Falls/Episodes/{}".format(url))
		print('downloading {}'.format(urllib.parse.unquote(url)))
		wget.download(url, '/Users/alikhundmiri/Desktop/Entertainment/TV/Gravity-falls/{}'.format(urllib.parse.unquote(url)))

if __name__ == '__main__':
	# main()
	download()
'''
http://51.15.61.24/Gravity%20Falls%20-%20S01E08%20-%20Irrational%20Treasure.mp4
http://51.15.61.24/Gravity%20Falls/Episodes/Gravity%20Falls%20-%20S01E08%20-%20Irrational%20Treasure.mp4
http://51.15.61.24/Gravity%20Falls/Episodes/Gravity%20Falls%20-%20S01E08%20-%20Irrational%20Treasure.mp4
http://51.15.61.24/Gravity%20Falls/Episodes/Gravity%20Falls%2520-%2520S01E08%2520-%2520Irrational%2520Treasure.mp4

'''