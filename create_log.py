import os
import sys
import datetime

def log_file(log_message, project_name, new_line, file_type):
	# print(project_name)
	if project_name==None:
		project_name = "general"
	else:
		project_name = project_name

	today_datetime = datetime.date.today()
	current_time = datetime.datetime.now()
	current_time_str = str('{:%I:%M:%S %p}'.format(current_time.time()))

	folder = '{}/logs/{}'.format(os.path.abspath(os.path.join(os.path.realpath(__file__), '..')),project_name)
	if not os.path.exists(folder):
		os.mkdir(folder)

	file_name = '{}/{}{}_{}.txt'.format(folder,'{:02d}'.format(today_datetime.month),'{:04d}'.format(today_datetime.year), file_type)
	
	with open(file_name,"a+") as f:
		# message = str(today_datetime) + "  " + log_message + "\n"
		message = '{} | {} - {}\n'.format(str(today_datetime), current_time_str, log_message)

		if new_line:
			message = "\n===============================================\n" + message
		f.write(message)

def log_error(log_message, project_name=None, new_line=False):
	log_file(log_message, project_name, new_line, "error")

def log_status(log_message, project_name=None, new_line=False):
	log_file(log_message, project_name, new_line, "logs")

if __name__ == '__main__':
	log_error("logging the first error", 'testing')
	log_status("logging the first status", 'testing')
