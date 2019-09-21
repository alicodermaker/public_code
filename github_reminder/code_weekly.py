import os, sys
from github import Github, GithubException
from credentials import user, password, access_token, apex_telegram_bot
import datetime 

sys.path.append(os.path.abspath(os.path.join(os.path.join(os.path.join(os.path.realpath(__file__), '..'), '..'),'..')))

# print(sys.path)
from public_code.credentials import TELEGRAM_TOKEN_METROREMINDER, PERSONAL_ID_TELEGRAM
from public_code.send_telegram_notification import send_message, custom_bot_admin
from public_code.create_log import log_error, log_status


def main():
	# First create a Github instance using an access token
	g = Github(access_token)
	user = g.get_user()
	# print(user.login)

	# Then play with your Github objects:
	last_update_repo = []
	date_today = datetime.datetime.now()

	log_message = "Scanning {} repo from account '@{}'".format((g.get_user().get_repos().totalCount), user.login)
	print(log_message)
	log_status(log_message, 'code_weekly', new_line=True)
	
	for repo in g.get_user().get_repos():
		try:
			commit = repo.get_commit(sha='master')
			last_commit = repo.name,commit.commit.committer.date
			# print("{}".format(type(last_commit[1])))
			delta = date_today - last_commit[1]
			last_update_repo.append(delta.days)
			# print("{} -- Last commit: {} days ago".format(repo.name,delta))
		except GithubException as e:
			# print(e)
			pass
	
	log_message = "Scan Complete!"
	print(log_message)
	log_status(log_message, 'code_weekly')

	last_update = min(last_update_repo)
	
	log_message = "Last commit, {} days ago.".format(last_update)
	print(log_message)
	log_status(log_message, 'code_weekly')
	
	if last_update < 3:
		log_message = "Notifying Admin."
		print(log_message)
		log_status(log_message, 'code_weekly')

		notify("You haven't push code in {} days".format(last_update), "How are you alive without coding?".format(last_update), "Long Time No Commit", 'Hero')

def notify(title, text, subtitle, Audio):
	message = '''
	*{}*
	{}
	_{}_
	'''.format(subtitle, text, title)
	try:
		custom_bot_admin(message, 'GitHub Reminder | Code Weekly', apex_telegram_bot)
	except Exception as e:
		log_error("Failed to send telegram message", 'code_weekly', new_line=True)
		print("failed")
		log_error(e, 'code_weekly', new_line=True)
		print(e)

	os.system("""osascript -e 'display notification "{}" with title "{}" subtitle "{}" sound name "{}"' """.format(title, subtitle, text, Audio))


if __name__ == '__main__':	
	main()