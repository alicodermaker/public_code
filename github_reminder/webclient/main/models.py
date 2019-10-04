from django.db import models
from django.conf import settings
from django.utils import timezone

import random
import string

# Create your models here.

'''
This app will keep track of
* all user's telegram ID
* Telegram bot api

and also
* send messages
'''

class accountCode(models.Model):
	app_name = "accountCode"

	# user profile
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

	# turn true if user is connected with telegram
	user_connected = models.BooleanField(default=False)

	# randomly generated code
	verify_code = models.CharField(max_length=10, unique=True, default=''.join(random.choice(string.ascii_letters) for i in range(10)))

	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return f'{self.user} {self.verify_code} - {self.user_connected}'

	class Meta:
		ordering = ["-timestamp", "-updated"]

	