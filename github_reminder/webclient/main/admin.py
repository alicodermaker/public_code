from django.contrib import admin

# Register your models here.
from .models import accountCode

class accountCodeAdmin(admin.ModelAdmin):
	list_display = [ 'user', 'user_connected', 'verify_code',]
	list_filter = ['user', 'user_connected', 'verify_code',]
	search_fields = ['user', 'user_connected', 'verify_code',]

admin.site.register(accountCode, accountCodeAdmin)