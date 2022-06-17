from django.urls import path

from firstapp.views import hellodjango, greeting, get_date, get_concrete_date

urlpatterns = [
    path('', hellodjango),
    path('<str:name>', greeting),
    path('date/', get_date),
    path('date/<str:date_format>', get_concrete_date)
]
