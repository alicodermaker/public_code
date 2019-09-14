from nltk.corpus import stopwords
import re

counts = dict()

def word_count(str):
	words = str.split()
	filtered_words = [word for word in words if word not in stopwords.words('english')]

	for word in filtered_words:
		if word in counts:
			counts[word] += 1
		else:
			counts[word] = 1

def analyse():
	for key, value in sorted(counts.items(), key=lambda item: item[1]):
		print("%s: %s" % (key, value))

def main():
	file_names = [
	'1977.txt', '1978.txt', '1979.txt', '1980.txt', '1981.txt', '1982.txt',
	'1983.txt', '1984.txt', '1985.txt', '1986.txt', '1987.txt', '1988.txt']
	
	for file_name in file_names:
		file1 = open('letters/'+file_name,"r+") 
		letter = file1.read().lower()

		clean_letter = re.sub('[^a-zA-Z0-9\n\.]', ' ', letter)

		file1.close()
		print("letter: {} letter length: {}".format(file_name, str(len(clean_letter))))
		word_count(clean_letter)

if __name__ == '__main__':
	main()
	analyse()