from django.urls import path

from bookstore.views import all_books, full_desc, get_book, get_author, get_authors_books

urlpatterns = [
    path('', all_books, name='all_books'),
    path('desc/<int:id>', full_desc, name='full_desc'),
    path('book/<int:id>', get_book),
    path('author/<int:id>', get_author, name='get_author'),
    path('authors_books/<int:id>', get_authors_books, name='get_authors_books')
]
