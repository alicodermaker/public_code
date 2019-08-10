import random
import time
import os
import datetime
import csv
import pandas

file_name = 'ListOfScrips.csv'

def main():
	df = pandas.read_csv(file_name)
	codes = df['Security Code']
	print(len(codes))
	# for code in codes:
		# print(code)

def fetch_code():
	df = pandas.read_csv(file_name)
	
	for key, value in df.iterrows(): 
		# stock_details(value['Security Code'])
		print(key)
		df.at[key,'current close'] = key



def stock_details(s_code):
	print("https://www.bseindia.com/stock-share-price/pentamedia-graphics-ltd/pentagraph/{}/".format(s_code))

	# print(s_code)
	high = 100
	current = 90
	low = 81

	return high, current, low

if __name__ == '__main__':
	# main()
	fetch_code()