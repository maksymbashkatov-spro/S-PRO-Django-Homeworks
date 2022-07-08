from django.db import models

from bookstore.views import authors, books


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

    class Meta:
        db_table = 'authors'

    @staticmethod
    def create_authors():
        for a in authors:
            author = Author(first_name=a['first_name'], last_name=a['last_name'], age=a['age'])
            author.save()


class Book(models.Model):
    title = models.CharField(max_length=150)
    released_year = models.IntegerField()
    description = models.TextField()
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = 'books'

    @staticmethod
    def create_books():
        for b in books:
            book = Book(title=b['title'], released_year=b['released_year'], description=b['description'],
                        author_id=Author.objects.get(id=b['author_id']))
            book.save()
