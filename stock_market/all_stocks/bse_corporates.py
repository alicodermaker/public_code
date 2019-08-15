from bsedata.bse import BSE
from re import sub
from decimal import Decimal
import random
import time
import os
import datetime
import csv
import pandas

file_name = 'ListOfScrips.csv'

def main():
	small_companies = []
	b = BSE()
	df = pandas.read_csv(file_name)
	codes = df['Security Code']
	# print(len(codes))
	for code in codes:
		q = b.getQuote(str(code))
		traded_value = q['totalTradedValue']
		marketCapFull = q['marketCapFull']
		marketCapFull_ = marketCapFull.split(" ")[0]
		traded_value_ = traded_value.split(" ")[0]
		if float(traded_value_) <= 0.99:
			small_companies.append(code)
			traded_value_int = Decimal(sub(r'[^\d.]', '', traded_value_))*10000000
			market_cap_int = Decimal(sub(r'[^\d.]', '', marketCapFull_))*10000000
			print("{} | stock : {} | Traded Value {} | Market Capital {}".format(q['companyName'], q['currentValue'], traded_value_int, market_cap_int))
		

def fetch_code():
	df = pandas.read_csv(file_name)
	
	for key, value in df.iterrows(): 
		# stock_details(value['Security Code'])
		print(value)
		df.at[key,'current close'] = key



def stock_details(s_code):
	print("https://www.bseindia.com/stock-share-price/pentamedia-graphics-ltd/pentagraph/{}/".format(s_code))

	# print(s_code)
	high = 100
	current = 90
	low = 81

	return high, current, low

if __name__ == '__main__':
	main()
	# fetch_code()