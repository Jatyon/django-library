from django.forms import ModelForm, IntegerField, CharField, DateField
from .models import Book, ExtraInfo, Author, Review
from django.core.validators import MinValueValidator

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publication_year']


class BookFormNew(ModelForm):
    publication_year = IntegerField(validators=[MinValueValidator(2000, message="Ksiązka nie może pochodzić sprzed 2000 roku!!!!")])
    class Meta:
        model = Book
        fields = ['title', 'publication_year']


class ExtraInfoForm(ModelForm):
    class Meta:
        model = ExtraInfo
        fields = '__all__'


class ExtraInfoForm2(ModelForm):
    class Meta:
        model = ExtraInfo
        exclude = ['book']


class ReviewForm2(ModelForm):
    class Meta:
        model = Review
        exclude = ['book']


class AuthorForm2(ModelForm):
    first_name = CharField(label='Autor: imię ')
    last_name = CharField(label='Autor: nazwisko ')
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']