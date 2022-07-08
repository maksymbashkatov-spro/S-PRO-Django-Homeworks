from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

    class Meta:
        db_table = 'authors'


class Book(models.Model):
    title = models.CharField(max_length=150)
    released_year = models.DateField()
    description = models.TextField()
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = 'books'
