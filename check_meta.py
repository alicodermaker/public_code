import PyOpenGraph

def check_url(url):

	og = PyOpenGraph(url)

	# print og.metadata # => {'url': 'http://www.rottentomatoes.com/m/10011268-oceans/', 'site_name': 'Rotten Tomatoes', 'image': 'http://images.rottentomatoes.com/images/movie/custom/68/10011268.jpg', 'type': 'movie', 'title': 'Oceans'}

	print(og.metadata['title']) # => Oceans

	print(og.is_valid()) # => return True or False

if __name__ == '__main__':
	check_url("http://ardizen.com/landing-page/index.html")
	check_url('http://www.rottentomatoes.com/m/10011268-oceans/')