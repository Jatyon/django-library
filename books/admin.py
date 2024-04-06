from django.contrib import admin
import books.models

admin.site.register(books.models.Book)
admin.site.register(books.models.Author)
admin.site.register(books.models.Category)
admin.site.register(books.models.ExtraInfo)
