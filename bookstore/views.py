from django.http import HttpRequest, HttpResponseNotFound
from django.shortcuts import render
from bookstore.models import Book, Author


def all_books(request: HttpRequest):
    books = Book.objects.all()
    if request.method == 'GET' and 'book_title' in request.GET:
        book_title = request.GET['book_title']
        books = books.filter(title=book_title)
    return render(request, 'bookstore/index.html', {'books': books})


def full_desc(request: HttpRequest, id):
    try:
        return render(request, 'bookstore/full_desc.html', {'description': Book.objects.get(pk=id).description})
    except:
        return HttpResponseNotFound(f'The description is not found, because the book with id {id} not found.')


def get_book(request: HttpRequest, id):
    return render(request, 'bookstore/get_book.html', {'book': Book.objects.get(pk=id)})


def get_author(request: HttpRequest, id):
    try:
        return render(request, 'bookstore/get_author.html', {'author': Author.objects.get(pk=id)})
    except:
        return HttpResponseNotFound(f'The author with id {id} not found.')


def get_authors_books(request: HttpRequest, id):
    authors_books = Book.objects.filter(author=id)
    author = Author.objects.get(pk=id)
    author = f'{author.first_name} {author.last_name}'
    try:
        return render(request, 'bookstore/authors_books.html', {'authors_books': authors_books, 'author': author})
    except:
        return HttpResponseNotFound(f'Books by this author is not found.')
