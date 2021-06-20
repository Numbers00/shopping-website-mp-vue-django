from django.contrib import admin

from .models import BookType, Author, Book

# Register your models here.
admin.site.register(BookType)
admin.site.register(Author)
admin.site.register(Book)