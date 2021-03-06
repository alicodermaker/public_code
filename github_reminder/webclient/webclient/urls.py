"""webclient URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

# from django.contrib.auth import views as auth_views

from main.views import login, home, send_message, desktop, all_accounts, friday_protocol

from telegrambot.views import message_reciever

urlpatterns = [
    path('', desktop),
    path('login/', login, name='login'),
    path('all_accounts/', all_accounts, name='all_accounts'),
    path('friday_protocol/', friday_protocol, name='friday_protocol'),
    path('send_message/', send_message, name='send_message'),
    path('accounts/profile/', home, name='home'),
    path('hook/', message_reciever),

    # path('logout/', auth_views.logout, name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
]