from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    authors = models.ManyToManyField(Author)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    extra_info = models.OneToOneField('ExtraInfo', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class ExtraInfo(models.Model):
    pages = models.IntegerField()
    language = models.CharField(max_length=50)
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return f"Pages: {self.pages}, Language: {self.language}, Publisher: {self.publisher}"


