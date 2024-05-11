from django.contrib import admin
from .models import Book, ExtraInfo, Review, Author

admin.site.register(Author)
admin.site.register(Review)
admin.site.register(ExtraInfo)

class ExtraInfoInline(admin.TabularInline):
    model = ExtraInfo

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0

class AuthorInline(admin.TabularInline):
    model = Author.books.through
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [ExtraInfoInline, ReviewInline, AuthorInline]
