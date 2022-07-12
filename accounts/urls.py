from django.contrib import admin
from django.urls import path, include

from accounts.views import RegisterFormView

urlpatterns = [
    path('register/', RegisterFormView.as_view(), name='register')
]
