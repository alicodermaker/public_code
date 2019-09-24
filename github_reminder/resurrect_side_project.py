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
	date_today = datetime.datetime.now()
	g = Github(access_token)
	user = g.get_user()
	joined_since = round((date_today - user.created_at).days / 365.25)

	# Then play with your Github objects:
	last_update_repo = []
	total_project = g.get_user().get_repos().totalCount
	log_message = "Scanning {} repo from account '@{}'".format(total_project, user.login)
	print(log_message)
	# log_status(log_message, 'resurrect_side_project', new_line=True)
	
	for repo in g.get_user().get_repos():
		try:
			commit = repo.get_commit(sha='master')
			last_commit = commit.commit.committer.date

			delta = date_today - last_commit
			# sort out project older than 120 days, and less than 30 days
			if 30 < delta.days < 120:
				commit_data = repo.name,repo.description,delta.days,
				last_update_repo.append(commit_data)
		except GithubException as e:
			# print(e)
			pass

	generate_message(last_update_repo, total_project, joined_since)


def generate_message(last_update_repo, total_project, joined_since):

	details = '''
	'''
	for project in last_update_repo:
		detail = '''
*{}*
_last commit {} days ago..._
Description: {}
		'''.format(project[0], project[2], project[1])
		details = detail + details

	message = '''
Hi, how are you?

I know this is awkard, but your exs reached out to me.
Listen, Im not going to force you to be with someone, I know it's your choice to _work it out_ or _leave it all_, but think about it man, every *side project* deserve better.

I understand, in the past *{} years*, you have been with *{} projects*. It's just who you are. I get it.
But you can move on like this!!!! 

If these are good projects, then I know for certain these {} deserve a second chance.

In case you forgot, this is what you thought of them when you first met them
{}

Sometimes all you need is break. I think you've had your break, long enough.
	'''.format(joined_since, total_project, len(last_update_repo), details)

	# print(message)
	custom_bot_admin(message, "crazy ex projects", apex_telegram_bot)
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
	# sort_data(commit_data)
	main()