from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, get_list_or_404

from bookstore.forms import CreateBookForm
from bookstore.models import Book, Author


def all_books(request: HttpRequest):
    books = Book.objects.all()
    if request.method == 'GET' and 'book_title' in request.GET:
        book_title = request.GET['book_title']
        books = books.filter(title=book_title)
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            title = data['title']
            released_year = data['released_year']
            description = data['description']
            author_id = data['author_id']
            Book.objects.create(title=title, released_year=released_year, description=description,
                                author=Author.objects.get(id=author_id))
    return render(request, 'bookstore/index.html', {'books': books})


def full_desc(request: HttpRequest, id):
    return render(request, 'bookstore/full_desc.html', {'description': get_object_or_404(Book, pk=id).description})


def get_book(request: HttpRequest, id):
    return render(request, 'bookstore/get_book.html', {'book': get_object_or_404(Book, pk=id)})


def get_author(request: HttpRequest, id):
    return render(request, 'bookstore/get_author.html', {'author': get_object_or_404(Author, pk=id)})


def get_authors_books(request: HttpRequest, id):
    authors_books = get_list_or_404(Book, author=id)
    author = Author.objects.get(pk=id)
    author = f'{author.first_name} {author.last_name}'
    return render(request, 'bookstore/authors_books.html', {'authors_books': authors_books, 'author': author})


def create_book(request):
    return render(request, 'bookstore/create_book.html', {'create_book_form': CreateBookForm})
