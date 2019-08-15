import pprint
from bsedata.bse import BSE
from small_cap import start as find_small


def main():
	b = BSE()
	# b = b.getScripCodes()
	indices = b.getIndices(category='market_cap/broad')
	pprint(indices)
	# find_small(indices)

if __name__ == '__main__':
	main()
