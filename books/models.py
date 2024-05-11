from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()

    def __str__(self):
        return "{} ({})".format(self.title, str(self.publication_year))
    
class ExtraInfo(models.Model):
    CATEGORY = {
        (0, 'Powiesc'),
        (1, 'Naukowa'),
        (2, 'Sci-fi'),
        (3, 'Dramat')
    }
    pages = models.IntegerField()
    category = models.PositiveSmallIntegerField(choices=CATEGORY,null=True, blank=True)
    language = models.CharField(max_length=50)
    publisher = models.CharField(max_length=100)
    book = models.OneToOneField(Book, on_delete=models.CASCADE, null=True, blank=True)  

    def __str__(self):
        for c in list(self.CATEGORY):
            if c[0] == self.category:
                gok = c[1]
        return "Book: {}, pages: {}, category: {}, language: {}, publisher: {}".format(self.book.title, 
                gok, self.pages, self.language,  self.publisher)


class Review(models.Model):
    notice = models.TextField(default="", blank=True)
    rate = models.PositiveSmallIntegerField(default=5)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True) 

    def __str__(self):
        rev = self.notice[:20] + ' ...'
        return "Book: {}, rate: {}, notice: {}".format(self.book.title, str(self.rate), rev)

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return "{} {}, jest autorem {} ksiązek z bazy danych".format(self.first_name, self.last_name, str(self.books.count()))








