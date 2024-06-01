from django.shortcuts import render, get_object_or_404,get_list_or_404, redirect
from django.http import HttpResponseRedirect
from books.models import Book, ExtraInfo, Review, Author
from books.forms import BookForm, BookFormNew, ReviewForm2, ExtraInfoForm2, AuthorForm2
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required,permission_required
from django.db.models import Count, Sum, Avg, Max, Min, Q

def all_books(request):
    books=Book.objects.all()
    context = {'books': books}
    return render(request, 'book/all-books.html', context)

def one_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    field_names = [b.name for b in Book._meta.get_fields()]
    for i,b in enumerate(field_names):
        if b == "review":
            field_names[i] = "review_set"
        elif b == "author":
            field_names[i] = "author_set"
        elif b == "extrainfo":
            field_names[i] = "extrainfo_set"
    return render(request, 'book/one-book.html', {'book': book, 'field_names': field_names})

@login_required
@permission_required("books.add_book")
def create_over_2000(request):
    form = BookFormNew(request.POST or None)
    form_einfo = ExtraInfoForm2(request.POST or None)
    form_review = ReviewForm2(request.POST or None)
    form_author = AuthorForm2(request.POST or None)
    if all([form.is_valid(), form_einfo.is_valid(), form_review.is_valid(), form_author.is_valid()]):
        book = form.save()
        einfo = form_einfo.save(commit=False)
        einfo.book = book
        einfo.save()
        review = form_review.save(commit=False)
        review.book = book
        review.save()
        author = form_author.save()
        author.books.add(book.id)
        author.save()
        return redirect(all_books)
    
    return render(request, 'book/create-book2.html', {'form': form, 'form_einfo':form_einfo, 'form_review': form_review, 'form_author': form_author})

@login_required
@permission_required("books.add_book")
def create_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(all_books)
    return render(request, 'book/create-book.html', {'form': form})

@login_required
@permission_required("books.add_book")
def create_book2(request):
    form = BookForm(request.POST or None)
    form_einfo = ExtraInfoForm2(request.POST or None)
    form_review = ReviewForm2(request.POST or None)
    form_author = AuthorForm2(request.POST or None)
    if all([form.is_valid(), form_einfo.is_valid(), form_review.is_valid(), form_author.is_valid()]):
        book = form.save()
        einfo = form_einfo.save(commit=False)
        einfo.book = book
        einfo.save()
        review = form_review.save(commit=False)
        review.book = book
        review.save()
        author = form_author.save()
        author.books.add(book.id)
        author.save()
        return redirect(all_books)
    
    return render(request, 'book/create-book2.html', {'form': form, 'form_einfo':form_einfo, 'form_review': form_review, 'form_author': form_author})

@login_required
@permission_required("books.change_book")
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect(all_books)
    return render(request, 'book/create-book.html', {'form':form})

@login_required
@permission_required("books.change_book")
def edit_book2(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    extra_info = get_object_or_404(ExtraInfo, book=book_id)
    review = get_list_or_404(Review, book=book_id)
    author = get_list_or_404(Author, books=book_id)

    form = BookForm(request.POST or None, instance=book)
    form_einfo = ExtraInfoForm2(request.POST or None,  instance=extra_info)
    form_review = ReviewForm2(request.POST or None, instance=review[0])
    form_author = AuthorForm2(request.POST or None, instance=author[0])
    if all([form.is_valid(), form_einfo.is_valid(), form_review.is_valid(), form_author.is_valid()]):
        book = form.save()
        einfo = form_einfo.save(commit=False)
        einfo.book = book
        einfo.save()
        review = form_review.save(commit=False)
        review.book = book
        review.save()
        author = form_author.save()
        author.books.add(book.id)
        author.save()
        return redirect(all_books)
    
    return render(request, 'book/create-book2.html', {'form': form, 'form_einfo':form_einfo, 'form_review': form_review, 'form_author': form_author})

@login_required
@permission_required("books.delete_book")
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method=="POST":
        book.delete()
        return redirect(all_books)
    return render(request, 'book/delete-book.html', {'book': book})

def logout_view(request):
  logout(request)
  return HttpResponseRedirect('/login')


@login_required
def books_category(request):
   books = Book.objects.all()
   booksNone = Book.objects.filter(extrainfo__category__isnull=True)
   category = ExtraInfo.CATEGORY
   context = {'books': books, 'category':category, 'booksNone':booksNone}
   print(context)
   return render(request, 'book/book-category.html', context)

@login_required
def stat_books(request):
    category = ExtraInfo.CATEGORY
    w =  Book.objects.all().aggregate(Count('id'))
    all = w['id__count']
    f = Book.objects.filter(extrainfo__category__isnull=True).aggregate(Count('id'))
    s = f['id__count']
    f0 = Book.objects.filter(extrainfo__category__exact=0).aggregate(Count('id'))
    s0 = f0['id__count']
    f1 = Book.objects.filter(extrainfo__category__exact=1).aggregate(Count('id'))
    s1 = f1['id__count']
    f2 = Book.objects.filter(extrainfo__category__exact=2).aggregate(Count('id'))
    s2 = f2['id__count']
    f3 = Book.objects.filter(extrainfo__category__exact=3).aggregate(Count('id'))
    s3 = f3['id__count']

    book_all = {('Wszystkie książki',all)}
    book_none = {('Ksiązki bez określonej kategorii', s)}
    books = {('Ksiązki z kategorii Powiesc', s0),
             ('Ksiązki z kategorii Naukowa', s1),
             ('Ksiązki z kategorii Sci-fi', s2),
             ('Ksiązki z kategorii Dramat', s3)}
    context = {'bookAll':book_all, 'bookNone':book_none, 'books':books, 'category':category}
    return render(request, 'book/stat-books.html', context)

@login_required
def authors_by_books(request):
    authors = Author.objects.all().annotate(l_books=Count('books')).order_by("-l_books")
    context = {'authors':authors}
    return render(request, 'book/stat-authors.html', context)