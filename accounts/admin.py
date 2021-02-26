from django.contrib import admin

# Register your models here.
from .models import CustomUser
from catalog.models import Author, Genre, Book, BookInstance, Language

admin.site.register(Author)
admin.site.register(Language)
admin.site.register(CustomUser)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(BookInstance)