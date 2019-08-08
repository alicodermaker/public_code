from create_logs import log_error, log_status

def main():
	log_error("logging the first error", 'lastmetro')
	log_status("logging the first status", 'lastmetro')

if __name__ == '__main__':
	main()