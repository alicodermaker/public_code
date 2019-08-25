from bs4 import BeautifulSoup
# from lxml import html
import os, requests

import datetime

now = datetime.datetime.now()

current_year = now.year
first_year = 1977

def main():
	for year in range(first_year, int(current_year-1)):
		year_link = 'https://www.berkshirehathaway.com/letters/{}.html'.format(year)
		file_name = '../letters/{}.txt'.format(year)

		html = requests.get(year_link)


		with open(file_name,"w+") as f:
			print("Writing... {} letter".format(year))
			message = ""
			f.write(message)

if __name__ == '__main__':
	main()