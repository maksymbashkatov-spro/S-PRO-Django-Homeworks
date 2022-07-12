from django.urls import path
from bookstore.views import create_book
from bookstore.views import BookView, AuthorDetailView, BookDetailView, FullDescDetailView, AuthorsBookListView

urlpatterns = [
    path('', BookView.as_view(), name='all_books'),
    path('desc/<int:pk>', FullDescDetailView.as_view(), name='full_desc'),
    path('book/<int:pk>', BookDetailView.as_view()),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='get_author'),
    path('authors_books/<int:pk>', AuthorsBookListView.as_view(), name='get_authors_books'),
    path('create_book', create_book)
]
