from django.http import HttpResponse
from django.http import HttpResponseRedirect
import django_filters.rest_framework
from rest_framework import generics
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from website.models import *
from website.serializers import *
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

# Create your views here.
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('ID','Title', 'Author','Category')

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('ID','User')

class issued(ModelViewSet):
    queryset = issueBook.objects.all()
    serializer_class = issueSerializer

@csrf_exempt
def issue(request):
    if request.method == "GET":
        books = Book.objects.filter(status = "Available")
        return render(request, 'issueForm.html',{'books':books})

    if request.method == "POST":
        bookId = request.POST['bookId']
        book = Book.objects.filter(bookID = bookId)[0]
        libraryUser = User.objects.filter(userID = 1)[0]
        noOfDays = request.POST['noOfDays']
        issueBook(Book = book, libraryUser = libraryUser, noOfDays = 3).save()
        book.status = "Issued"
        book.save()
        return HttpResponseRedirect('/book')

@csrf_exempt
def returnBook(request):
    if request.method == "GET":
        books = Book.objects.filter(status = "Issued")
        return render(request, 'returnForm.html',{'books':books})

    if request.method == "POST":
        bookId = request.POST['bookId']
        book = Book.objects.filter(bookID = bookId)[0]
        book.status = "Available"
        book.save()
        return HttpResponseRedirect('/book')
