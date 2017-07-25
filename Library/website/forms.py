from django import forms
from .models import *

book = Book.objects.all()
books = [[x.bookID,x.Title] for x in book.filter(status = "0")]

class IssueBook(forms.Form):
    book = forms.MultipleChoiceField(choices=books, required=True)
    noOfDays = forms.IntegerField()
    userId = forms.CharField(max_length = 100)
