from django.contrib import admin

from .models import telegramAccount, messageBuffer#, messageLogs


class telegramAccountAdmin(admin.ModelAdmin):
	list_display = ['user', 'id_user', 'first_name', 'last_name']
	list_filter = ['user', 'id_user', 'first_name', 'last_name']
	search_fields = ['user', 'id_user', 'first_name', 'last_name']

# class messageLogsAdmin(admin.ModelAdmin):
# 	list_display = [ 'id_user', 'first_name', 'last_name']
# 	list_filter = ['id_user', 'first_name', 'last_name']
# 	search_fields = ['id_user', 'first_name', 'last_name']

class messageAdmin(admin.ModelAdmin):
	list_display = [ 'user_id', 'first_name', 'last_name']
	list_filter = ['user_id', 'first_name', 'last_name']
	search_fields = ['user_id', 'first_name', 'last_name']

admin.site.register(telegramAccount, telegramAccountAdmin)
# admin.site.register(messageLogs, messageLogsAdmin)
admin.site.register(messageBuffer, messageAdmin)