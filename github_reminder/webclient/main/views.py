from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from github import Github, GithubException
import datetime 
import uuid 

from social_django.models import UserSocialAuth
from telegrambot.models import telegramAccount
from .models import accountCode
from .forms import UserVerifyForm
from .weekly_reminder import gather_github_data

def desktop(request):
	'''Opens the simple landing page'''
	
	return render(request, 'main/desktop.html')

@login_required
def home(request):
	'''user profile page. If this is the first time a user is logging in, a Verification code will be created for them.'''
	user = request.user

	try:
		user_verify = accountCode.objects.get(user=user)
	except Exception as e:
		# print("user not found, creating form")

		form = UserVerifyForm(request.POST or None)
	
		if form.is_valid():
			print('form is valid')
		else:
			print('form is not valid')
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			return HttpResponseRedirect(reverse('home'))

	try:
		github_login = user.social_auth.get(provider='github')
	except UserSocialAuth.DoesNotExist:
		github_login = None

	# g = Github(github_login.extra_data['access_token'])

	context = {
		'github_login' : github_login,
		'user_connected' : user_verify.user_connected,
		'verification_code' : user_verify.verify_code,
	}
	return render(request,'main/homepage.html', context)

@login_required
def send_message(request):
	logged_user = request.user

	try:
		github_login = logged_user.social_auth.get(provider='github')
	except UserSocialAuth.DoesNotExist:
		github_login = None

	core_script(github_login)

	context = {
		'github_login' : github_login
	}
	return render(request,'main/send_message.html', context)

def core_script(github_login):
	# print(github_login.extra_data['access_token'])
	date_today = datetime.datetime.now()
	
	g = Github(github_login.extra_data['access_token'])
	user = g.get_user()
	joined_since = round((date_today - user.created_at).days / 365.25)

	# last_update_repo = []
	all_projects = g.get_user().get_repos()
	total_project = all_projects.totalCount
	print("total projects: {}".format(total_project))
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

def login(request):
	'''Login page'''
	return render(request, 'main/login.html')

@user_passes_test(lambda u: u.is_superuser)
def all_accounts(request):
	''' Simple over view of all the accounts '''
	telegram_count = telegramAccount.objects.all().count()
	github_count = UserSocialAuth.objects.filter(provider='github').count()

	context = {
		'telegram_count' : telegram_count,
		'github_count' : github_count,
	}
	return render(request, 'main/all_accounts.html', context)

@user_passes_test(lambda u: u.is_superuser)
def friday_protocol(request):
	''' friday_protocol : gather information '''
	gather_github_data()

	# after this is done, load the data from models where all instances are saved.
	telegram_count = telegramAccount.objects.all().count()
	github_count = UserSocialAuth.objects.filter(provider='github').count()

	context = {
		'telegram_count' : telegram_count,
		'github_count' : github_count,
	}
	return render(request, 'main/all_accounts.html', context)