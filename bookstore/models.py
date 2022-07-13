from django.contrib.auth import get_user_model
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

    class Meta:
        db_table = 'authors'

    def __str__(self):
        return f'{self.first_name} | {self.last_name} | {self.age}'

    # @staticmethod
    # def create_authors():
    #     for a in authors:
    #         author = Author(first_name=a['first_name'], last_name=a['last_name'], age=a['age'])
    #         author.save()


class Book(models.Model):
    title = models.CharField(max_length=150)
    released_year = models.IntegerField()
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank='true', null='true')

    def __str__(self):
        return f'{self.title} | {self.released_year} | {self.description} | {self.author}'

    class Meta:
        db_table = 'books'

    # @staticmethod
    # def create_books():
    #     for b in books:
    #         book = Book(title=b['title'], released_year=b['released_year'], description=b['description'],
    #                     author_id=Author.objects.get(id=b['author_id']))
    #         book.save()


class Review(models.Model):
    text = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank='true', null='true')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank='true', null='true')

    class Meta:
        db_table = 'reviews'
