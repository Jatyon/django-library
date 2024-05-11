# from django.test import TestCase, Client
# from django.urls import reverse, resolve
# from django.contrib.auth.models import User
# from .views import all_books, one_book, create_book, edit_book, delete_book, nowy_nowy, create_book2
# from .models import Book, ExtraInfo, Author, Category

# class BooksTests(TestCase):
#     def setUp(self):
#         User.objects.create_superuser(username='admin', password='admin')

# # Test urls
#     def test_urls_all_books(self):
#         url = reverse('')
#         # print(resolve(url))
#         self.assertEquals(resolve(url).func, all_books)

#     def test_urls_one_book(self):
#         url = reverse('', args=[61])
#         self.assertEquals(resolve(url).func, one_book)

#     def test_urls_nowy(self):
#         url = reverse('create')
#         self.assertEquals(resolve(url).func, create_book)

#     def test_urls_nowy_nowy(self):
#         url = reverse('nowy_nowy')
#         self.assertEquals(resolve(url).func, nowy_nowy)

#     def test_urls_nowy2(self):
#         url = reverse('nowy2')
#         self.assertEquals(resolve(url).func, create_book2)

#     def test_urls_edytuj_film(self):
#         url = reverse('edit', args=[31])
#         self.assertEquals(resolve(url).func, edit_book)

#     def test_urls_usun(self):
#         url = reverse('delete', args=[3])
#         self.assertEquals(resolve(url).func, delete_book)

# # Test views

#     def test_views_all_books(self):
#         client = Client()
#         response = client.get(reverse(''))
#         self.assertEquals(response.status_code,200)

#     def test_views_all_books_templates(self):
#         client = Client()
#         response = client.get(reverse('wszystkie'))
#         self.assertTemplateUsed(response, 'book/all-books.html')

#     def test_views_one_book(self):
#         Book.objects.create(title="Ksiazka testowa", publication_year=2010)
#         client = Client()
#         response = client.get(reverse('', args=[1]))
#         self.assertEquals(response.status_code, 200)

#     def test_views_one_book_templates(self):
#         Book.objects.create(title="Ksiazka testowa", publication_year=2010)
#         client = Client()
#         response = client.get(reverse('', args=[1]))
#         self.assertTemplateUsed(response, 'book/one-book.html')

#     def test_views_create(self):
#         client = Client()
#         client.login(username="admin", password="admin")
#         response = client.get(reverse('create'))
#         self.assertEquals(response.status_code, 200)

#     def test_views_create_templates(self):
#         client = Client()
#         client.login(username="admin", password="admin")
#         response = client.get(reverse('create'))
#         self.assertTemplateUsed(response, 'book/create-book.html')

#     def test_views_edit(self):
#         book = Book.objects.create(title="Ksiazka testowa", publication_year=2010)
#         client = Client()
#         client.login(username="admin", password="admin")
#         response = client.get(reverse('edit', args=[1]))
#         self.assertEquals(response.status_code, 200)

#     def test_views_edit_templates(self):
#         book = Book.objects.create(title="Ksiazka testowa", publication_year=2010)
#         client = Client()
#         client.login(username="admin", password="admin")
#         response = client.get(reverse('edit', args=[1]))
#         self.assertTemplateUsed(response, 'book/create-book.html')

#     def test_views_delete(self):
#         book = Book.objects.create(title="Ksiazka testowa", publication_year=2010)
#         client = Client()
#         client.login(username="admin", password="admin")
#         response = client.get(reverse('delete', args=[1]))
#         self.assertEquals(response.status_code, 200)

#     def test_views_delete_templates(self):
#         book = Book.objects.create(title="Ksiazka testowa", publication_year=2010)
#         client = Client()
#         client.login(username="admin", password="admin")
#         response = client.get(reverse('delete', args=[1]))
#         self.assertTemplateUsed(response, 'book/delete-book.html')

# # Test models
#     def test_models_book_as_text(self):
#         book = Book.objects.create(title="Ksiazka testowa", publication_year=2010)
#         self.assertEquals(str(book), "{} ({})".format(book.title, str(book.publication_year)))

#     def test_models_new_book_not_empty(self):
#         book = Book.objects.create(title="Ksiazka testowa", publication_year=2010)
#         self.assertNotEquals(book, None)

#     def test_models_book_is_unique(self):
#         book = Book.objects.create(title="Ksiazka testowa", publication_year=2010)
#         with self.assertRaises(Exception):
#             book2 = Book.objects.create(title="Ksiazka testowa", publication_year=2010)

#     def test_models_only_one_new_book(self):
#         Book.objects.create(title="Ksiazka testowa", publication_year=2010)
#         self.assertEquals(Book.objects.all().count(), 1)

#     # def test_models_extrainfo_in_choise(self):
#     #     GATUNEK = [0, 1, 2, 3, 4]
#     #     einfo = ExtraInfo.objects.create(gatunek=1, czas_trwania=90)
#     #     self.assertIn(einfo.gatunek, GATUNEK)