
from social_django.models import UserSocialAuth
from github import Github, GithubException

from telegrambot.models import telegramAccount#, messageLogs, messageBuffer
import datetime 

''' This file contains code to send weekly messages'''

'''
	Method 1:
	1. Go in loop and Get data from all user information [telegram and github]
	2. Store it in our database
	3. Go in another loop and Send all messages

	This require a new class in models

	Method 2:
	1. Go in loop, get User information [telegram and github]
	2. within the loop, get user github information
	3. Send telegram message to user, and store information to models

'''

def gather_github_data():
	'''main control panel'''
	print("\tOK\t\tStarting to gather user data")
	get_users()
	

def get_users():
	''' generate message based on user's github account, after fetching their telegram data'''
	'''get a list of users who have completed registration. 
	i.e. signed up on github and we have their telegram'''

	# get telegram users list
	telegram_users = telegramAccount.objects.all()
	print("\tOK\t\t{} User's data gathered".format(telegram_users.count()))

	# for all users, find their github accounts on our database.
	# This is required to fetch their saved access tokens
	# print(telegram_users)
	i = 1
	for user in telegram_users:
		print('\tOK\t\tScanning user --- {}/{}'.format(i, telegram_users.count()))
		logged_user = user.user
		try:
			github_login = logged_user.social_auth.get(provider='github')
			print("\tOK\t\tgot github account")
		except UserSocialAuth.DoesNotExist:
			github_login = None
			print("\tERROR\t\tfailed to get github account")
			# maybe Admin (me) should get message, here based on what happens here?

		message = github_data(github_login)
		print("\tOK\t\tmessage generated")
		# save_data(message, user)
		i += 1

def github_data(github_login):
	# print(github_login.extra_data['access_token'])
	date_today = datetime.datetime.now()
	
	g = Github(github_login.extra_data['access_token'])
	
	print("\tOK\t\tfetching user projects")
	
	all_projects = g.get_user().get_repos()
	total_project = all_projects.totalCount
	
	print("\tOK\t\tfound {} projects".format(total_project))
	
	last_update_repo = []
	print("\tOK\t\tPlease wait... looking for Abandoned projects. might take a while...")
	for repo in all_projects:
		try:
			commit = repo.get_commit(sha='master')
			last_commit = commit.commit.committer.date
			delta = date_today - last_commit
			# sort out project older than 120 days, and less than 30 days
			if 30 < delta.days < 120:
				commit_data = repo.name,repo.description,delta.days
				# print(commit_data)
				# print(repo)
				last_update_repo.append(commit_data)
		except GithubException as e:
			# print(e)
			pass
	print("\tOK\t\tgot {} abandoned projects".format(len(last_update_repo)))
	message = generate_message(last_update_repo, total_project)
	# print(message)
	return message


def generate_message(last_update_repo, total_project):
	print("\tOK\t\tgenerating messsage...")
	details = '''
	'''
	for project in last_update_repo:
		detail = '''
*{}*
_last commit {} days ago..._
*Description*: {}
		'''.format(project[0], project[2], project[1])
		details = detail + details

	message = '''
Total Projects So far: *{}*

Found _*{}*_ Abandoned projects for your to think about:
{}

_Sometimes all you need is Break and Distance to understand the meaning._
	'''.format(total_project, len(last_update_repo), details)
	return message
	
'''
def save_data(message, user):
	print("\tOK\t\tsaving message and user into to database")
	entry = messageBuffer.objects.create(
		id_user = user.user_id,
		message = message,
		first_name = user.first_name,
		last_name = user.last_name)
	entry.save()
	print("\tCOMPLETE\t\tMessage Generated and Saved")
'''
	

def send_message(github_login):
	# print(github_login.extra_data['access_token'])
	date_today = datetime.datetime.now()
	
	g = Github(github_login.extra_data['access_token'])
	# user = g.get_user()
	# joined_since = round((date_today - user.created_at).days / 365.25)

	# last_update_repo = []
	all_projects = g.get_user().get_repos()
	total_project = all_projects.totalCount
	print("total projects: {}".format(total_project))
	'''
	for repo in all_projects:
		try:
			commit = repo.get_commit(sha='master')
			last_commit = commit.commit.committer.date

			delta = date_today - last_commit
			# sort out project older than 120 days, and less than 30 days
			if 30 < delta.days < 120:
				# commit_data = repo.name,repo.description,delta.days
				# print(commit_data)
				print(type(repo))
				# last_update_repo.append(commit_data)
		except GithubException as e:
			# print(e)
			pass
	# generate_message(last_update_repo, total_project, joined_since)
	'''


# gather_github_data()
# if __name__ == '__main__':
# 	gather_github_data()