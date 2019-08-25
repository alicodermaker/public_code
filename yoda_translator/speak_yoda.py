import requests

def main(input_message):
	url = 'https://api.funtranslations.com/translate/yoda.json?text=' + input_message
	r = requests.get(url)	

	try:
		out_message = r.json()['contents']['translated']
		print("yoda said: {}".format(out_message))
	except:
		print(r.json())

if __name__ == '__main__':
	input_message = raw_input("Say something...: ")
	main(input_message)