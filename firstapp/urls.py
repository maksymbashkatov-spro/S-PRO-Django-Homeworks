from django.urls import path

from firstapp.views import hellodjango, greeting

urlpatterns = [
    path('', hellodjango),
    path('<str:name>', greeting)
]
