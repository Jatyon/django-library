from django.urls import path
from .views import all_books, one_book, create_book, edit_book, delete_book

urlpatterns = [
    path('', all_books, name='all_books'),
    path('<int:book_id>/', one_book, name='one_book'),
    path('create/', create_book, name='create_book'),
    path('edit/<int:book_id>/', edit_book, name='edit_book'),
    path('delete/<int:book_id>/', delete_book, name='delete_book')
]
