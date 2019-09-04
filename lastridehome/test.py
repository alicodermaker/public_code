
'''
This two line of code, add parent directory to PYTHONPATH. 
Important for relative import of create_log file
'''
import sys
sys.path.insert(0,'..')

from public_code.create_log import log_error, log_status

def main():
	log_error("logging the first error", 'lastmetro')
	log_status("logging the first status", 'lastmetro')

if __name__ == '__main__':
	main()