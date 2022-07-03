from django.http import HttpRequest
from django.shortcuts import render

books = [{'id': 1,
          'title': 'Fluent Python',
          'released_year': 2015,
          'description': 'Python’s simplicity lets you become productive quickly, but this often means you aren’t '
                         'using everything it has to offer. With this hands-on guide, you’ll learn how to write '
                         'effective, idiomatic Python code by leveraging its best—and possibly most '
                         'neglected—features. Author Luciano Ramalho takes you through Python’s core language features '
                         'and libraries, and shows you how to make your code shorter, faster, and more readable '
                         'at the same time.',
          'author_id': 1},
         {'id': 2,
          'title': 'title2',
          'released_year': 2001,
          'description': 'Description2description2description2description2description2description2. '
                         'Description2description2description2description2description2description2.',
          'author_id': 2},
         {'id': 3,
          'title': 'title3',
          'released_year': 2010,
          'description': 'Description3description3description3description3description3description3. '
                         'Description3description3description3description3description3description3.',
          'author_id': 1},
         {'id': 4,
          'title': 'title4',
          'released_year': 2011,
          'description': 'Description4description4description4description4description4description4. '
                         'Description4description4description4description4description4description4.',
          'author_id': 3},
         {'id': 5,
          'title': 'title5',
          'released_year': 2015,
          'description': 'Description5description5description5description5description5description5. '
                         'Description5description5description5description5description5description5.',
          'author_id': 2}]

authors = [{'id': 1, 'first_name': 'Luciano', 'last_name': 'Ramalho', 'age': 51},
           {'id': 2, 'first_name': 'FirstName2', 'last_name': 'LastName2', 'age': 40},
           {'id': 3, 'first_name': 'FirstName3', 'last_name': 'LastName3', 'age': 37}]


def all_books(request: HttpRequest):
    return render(request, 'bookstore/index.html', {'books': books})


def full_desc(request: HttpRequest, id):
    return render(request, 'bookstore/full_desc.html', {'description': books[id - 1]['description']})


def get_book(request: HttpRequest, id):
    return render(request, 'bookstore/get_book.html', {'book': books[id - 1]})


def get_author(request: HttpRequest, id):
    return render(request, 'bookstore/get_author.html', {'author': authors[id - 1]})
