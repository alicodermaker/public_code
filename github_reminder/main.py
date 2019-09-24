import os, sys
import datetime 
from github import Github, GithubException
from credentials import user, password, access_token

sys.path.append(os.path.abspath(os.path.join(os.path.join(os.path.join(os.path.realpath(__file__), '..'), '..'),'..')))

from public_code.credentials import TELEGRAM_TOKEN_METROREMINDER, PERSONAL_ID_TELEGRAM
from public_code.send_telegram_notification import send_message
from public_code.create_log import log_error, log_status

def alert_for_admin():
	'''First create a Github instance using an access token'''
	g = Github(access_token)
	user = g.get_user()
	# print(user.login)

	# Then play with your Github objects:
	last_update_repo = []
	date_today = datetime.datetime.now()
	# print("Scanning your repos... Please wait")

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

	last_update = min(last_update_repo)
	# print(last_update)

	if last_update > 3:
		# print("More than 3 days since your commit. Notifying Admin.")
		notify("You havent written commits in {} days".format(last_update), "How are you lived past {} days?".format(last_update), "Long Time No Commit", 'Hero')

def notify(title, text, subtitle, Audio):
	send_message(title, text, subtitle)
	os.system("""osascript -e 'display notification "{}" with title "{}" subtitle "{}" sound name "{}"'""".format(title, subtitle, text, Audio))

if __name__ == '__main__':
	alert_for_admin()


'''
Cronjob : run everyday, at 12.

0 12 * * * /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7 /Users/alikhundmiri/Desktop/pythons/alicodermaker/public_code/github_reminder/main.py

'''