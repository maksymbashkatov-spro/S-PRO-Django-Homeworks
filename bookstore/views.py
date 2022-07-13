from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView

from bookstore.forms import CreateBookForm, CreateReviewForm
from bookstore.models import Book, Author, Review
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


class AllBookView(View):
    def get(self, request):
        books = Book.objects.all()
        if 'book_title' in request.GET:
            book_title = request.GET['book_title']
            books = books.filter(title=book_title)
        return render(request, 'bookstore/index.html', {'books': books})

    def post(self, request):
        books = Book.objects.all()
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


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'bookstore/get_author.html'


# class BookDetailView(DetailView):
#     model = Book
#     template_name = 'bookstore/get_book.html'


def get_book(request: HttpRequest, id):
    if request.method == 'POST':
        form = CreateReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            text = data['text']
            print('XXX', Book.objects.get(pk=id))
            Review.objects.create(text=text, book=Book.objects.get(pk=id), user=request.user)
    return render(request, 'bookstore/get_book.html', {'book': get_object_or_404(Book, pk=id),
                                                       'create_review_form': CreateReviewForm,
                                                       'reviews': Review.objects.all()})


class FullDescDetailView(DetailView):
    model = Book
    template_name = 'bookstore/full_desc.html'


class AuthorsBookListView(ListView):
    template_name = 'bookstore/authors_books.html'

    def get_queryset(self):
        self.author = get_object_or_404(Author, id=self.kwargs['pk'])
        return Book.objects.filter(author=self.author)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = f'{self.author.first_name} {self.author.last_name}'
        return context


def create_book(request):
    return render(request, 'bookstore/create_book.html', {'create_book_form': CreateBookForm})
