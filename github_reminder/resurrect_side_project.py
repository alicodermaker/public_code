import os, sys
from github import Github, GithubException
from credentials import user, password, access_token, apex_telegram_bot
import datetime 

sys.path.append(os.path.abspath(os.path.join(os.path.join(os.path.join(os.path.realpath(__file__), '..'), '..'),'..')))

# print(sys.path)
from public_code.credentials import TELEGRAM_TOKEN_METROREMINDER, PERSONAL_ID_TELEGRAM
from public_code.send_telegram_notification import send_message, custom_bot_admin
from public_code.create_log import log_error, log_status

commit_data = [
('public_code', 0),
('ACM_challenge_1', 217),
('afiio', 457),
('alireviewstuff', 356),
('automated_emailer', 831),
('BasicallyTwins', 547),
('bitcoin_on_amazon', 638),
('chat-Remainder', 825),
('Cur-Den', 1046),
('dailylauncher', 623),
('edu-tour', 1078),
('everything', 19),
('gitignore', 237),
('gravity_falls', 772),
('hacker-scripts', 865),
('housekeeping', 233),
('idea_cm', 671),
('image_manuplation', 131),
('iniglobal', 997),
('ini_alpha', 894),
('inpsyght', 362),
('insta2blog', 234),
('instabot.py', 745),
('mera_personal', 25),
('mindhacking', 779),
('my-work-list', 463),
('nasa_quote_website', 92),
('Paytm_Web_Sample_Kit_Python', 851),
('personal-goals', 465),
('poetist', 763),
('Popular-Movies-1', 999),
('Portfolio', 1125),
('private_code', 7),
('professional', 1032),
('PyCyanide', 1955),
('python-aws-s3', 719),
('PyWhatsapp', 1166),
('qnapps', 471),
('quora_chores', 831),
('Rename-Files', 961),
('Resume-Forwarder', 1011),
('revenue_source_directory', 362),
('ritrew', 642),
('save_PIL_to_S3', 524),
('sententia', 919),
('simple_site', 542),
('smm', 339),
('starplayschool', 545),
('stock_market', 50),
('subtitle-downloader', 1083),
('Sunshine', 1072),
('testing_222', 205),
('Tutorials', 1300),
('twitter_user_engagement', 467),
('vrajrv', 204),
('woodwatchtime', 911),
('ytpomodoro', 98),
('ardizen_website_2019', 155),
('Workplace', 16),

]

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
	# log_status(log_message, 'resurrect_side_project', new_line=True)
	
	for repo in g.get_user().get_repos():
		try:
			commit = repo.get_commit(sha='master')
			last_commit = commit.commit.committer.date
			# print("{}".format((last_commit)))

			delta = date_today - last_commit
			commit_data = repo.name,delta.days
			last_update_repo.append(commit_data)
			# print("{} -- Last commit: {} days ago".format(repo.name,delta))
		except GithubException as e:
			# print(e)
			pass

	for repo in last_update_repo:
		print(repo)

def sort_data(commit_data):
	sorted_list = sorted(commit_data,reverse = True , key = lambda x: x[1])
	for item in sorted_list:
		print(item)

def notify(title, text, subtitle, Audio):
	message = '''
	*{}*
	{}
	_{}_
	'''.format(subtitle, text, title)
	try:
		custom_bot_admin(message, 'GitHub Reminder | Resurrect Side Project', apex_telegram_bot)
	except Exception as e:
		log_error("Failed to send telegram message", 'resurrect_side_project', new_line=True)
		print("failed")
		log_error(e, 'resurrect_side_project', new_line=True)
		print(e)
	os.system("""osascript -e 'display notification "{}" with title "{}" subtitle "{}" sound name "{}"' """.format(title, subtitle, text, Audio))


if __name__ == '__main__':
	sort_data(commit_data)
	# main()