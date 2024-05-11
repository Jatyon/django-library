from django.urls import path
from .views import all_books, one_book, create_book, edit_book, delete_book, create_over_2000, create_book2, edit_book2,books_category,stat_books,authors_by_books

urlpatterns = [
    path('', all_books, name='all_books'),
    path('<int:book_id>/', one_book, name='one_book'),
    path('create/', create_book, name='create_book'),
    path('create2/', create_book2, name='create_book2'),
    path('create3/', create_over_2000, name='create_over_2000'),
    # path('edit/<int:book_id>/', edit_book, name='edit_book'),
    path('edit/<int:book_id>/', edit_book2, name='edit_book2'),
    path('delete/<int:book_id>/', delete_book, name='delete_book'),
    path('books_category/', books_category, name='books_category'),
    path('stat_books/', stat_books, name='stat_books'),
    path('stat-authors/', authors_by_books, name='authors_by_books'),
]
