from django.urls import path

from firstapp.views import hellodjango

urlpatterns = [
    path('', hellodjango),
]
