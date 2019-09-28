from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

'''
This app will keep track of
* all user's telegram ID
* Telegram bot api

and also
* send messages
'''

class telegramAccount(models.Model):
    app_name = "telegramAccount"
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

    id_user     = models.IntegerField(unique=True, primary_key=True)
    first_name  = models.CharField(max_length=64)
    last_name   = models.CharField(max_length=64)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    # def get_absolute_url(self):
    #     return reverse("blogs:detail", kwargs={"slug" : self.slug})

    class Meta:
        ordering = ["-timestamp", "-updated"]


class messageLogs(models.Model): 
    id_user     = models.IntegerField(unique=True, primary_key=True)
    first_name  = models.CharField(max_length=64)
    last_name   = models.CharField(max_length=64)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ["-timestamp", "-updated"]

class Message(models.Model):
    update_id       = models.IntegerField(unique=True)
    text            = models.TextField(max_length=4096)
    date            = models.DateTimeField(default=timezone.now)
    sender          = models.ForeignKey(messageLogs, on_delete=models.CASCADE)
 
    def __str__(self):
        return f'{self.text}'