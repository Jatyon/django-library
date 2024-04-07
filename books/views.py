from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect
from books.models import Book
from books.forms import BookForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def all_books(request):
    books=Book.objects.all()
    context = {'books': books}
    return render(request, 'book/all-books.html', context)

def one_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    field_names = [b.name for b in Book._meta.get_fields()]
  
    for i,b in enumerate(field_names):
        print(b)
        if b == "category":
            field_names[i] = "category_set"
        elif b == "authors":
            field_names[i] = "authors_set"
    print(field_names)
    return render(request, 'book/one-book.html', {'book': book, 'field_names': field_names})

@login_required
def create_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(all_books)
    return render(request, 'book/create-book.html', {'form': form})

@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect(all_books)
    return render(request, 'book/create-book.html', {'form':form})

@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method=="POST":
        book.delete()
        return redirect(all_books)
    return render(request, 'book/delete-book.html', {'book': book})

def logout_view(request):
  logout(request)
  return HttpResponseRedirect('/login')