from bsedata.bse import BSE

b = BSE()
q = b.getQuote(str(532454))

print("company Name 		 : {}".format(q['companyName']))
print("--------------------------------------------")
print("current Value 		 : {}".format(q['currentValue']))
print("52 week High 		 : {}".format(q['52weekHigh']))
print("52 week Low  	  	 : {}".format(q['52weekLow']))
print("totat Traded Value 	 : {}".format(q['totalTradedValue']))
print("total Traded Quantity : {}".format(q['totalTradedQuantity']))