from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book

def all_books(request):
    books=Book.objects.all()
    context = {'books': books}
    print(context)
    return render(request, 'book/all.html', context)

def details(request, book_id):
    b = Book.objects.get(id=book_id)
    return HttpResponse("<h3> Tytuł Książki: {},</br> rok wydania: {} </h3>".format(b.title,b.publication_year))
