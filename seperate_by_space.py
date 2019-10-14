
def main():
	''' With messages, take an see if the message is with special string '''
	messages = ["/start Adr3Frew4", "/start", "/start GrY6Lo7g"]
	for message in messages:
		seperate = message.split(" ")
		print(len(seperate))

if __name__ == '__main__':
	main()