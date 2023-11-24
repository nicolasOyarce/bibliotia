from django.forms import ModelForm, forms
#from .models import Books

class BooksForm(ModelForm):

    class Meta:
        model = Books
        fields = ['name', 'author','editorial', 'description', 'used', 'price', 'quantity', 'image']