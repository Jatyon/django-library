from django.urls import path
from .views import all_books,details

urlpatterns = [
    path('all-books/', all_books, name='all-books'),
    path('details/<int:book_id>/', details),
]
