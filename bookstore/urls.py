from django.urls import path

from bookstore.views import all_books, full_desc

urlpatterns = [
    path('', all_books),
    path('desc/<int:id>', full_desc, name='full_desc')
]
