from django.contrib import admin

# Register your models here.

import .models import Genre, Author, Book, Osoba, Stanowisko

admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Osoba)
admin.site.register(Stanowisko)