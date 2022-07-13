from django.contrib import admin
from .models import Author, Book, Review


class AuthorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Author._meta.fields]
    search_fields = [field.name for field in Author._meta.fields]
    list_filter = ['first_name', 'last_name', 'age']
    list_editable = ['first_name', 'last_name', 'age']


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'released_year', 'description', 'author']
    search_fields = ['title', 'released_year', 'description', 'author__age']
    list_filter = ['title', 'released_year', 'description']
    list_editable = ['title', 'released_year', 'description']


admin.site.register(Book, BookAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'book', 'user']
    search_fields = ['text']
    list_filter = ['text']
    list_editable = ['text']


admin.site.register(Review, ReviewAdmin)
