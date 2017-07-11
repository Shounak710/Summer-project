from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
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
from .forms import *
from django.shortcuts import get_object_or_404
# Create your views here.
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('bookID','Title', 'Author','Genre')

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('userID','User')

class issued(ModelViewSet):
    queryset = issueBook.objects.all()
    serializer_class = issueSerializer

def userRecord(request , userId):
    user = User.objects.filter(userID = userId)
    issuedBook = issueBook.objects.filter(libraryUser = user)
    return render(request, 'user.html',{'issuedBook':issuedBook})

@csrf_exempt
def issue(request):
    if request.method == "POST":
        form = IssueBook(request.POST)
        if form.is_valid():
            bookId = form.cleaned_data['book']
            userId = form.cleaned_data['userId']
            noOfDays = form.cleaned_data['noOfDays']
            book = Book.objects.get(bookID = str(bookId)[2:-2])
            libraryUser = User.objects.filter(userID = userId)[0]
            issueBook(Book = book, libraryUser = libraryUser, noOfDays = noOfDays).save()
            book.status = "1"
            book.save()
            return HttpResponse("Successfully issued")

    else:
        form = IssueBook()
        return render(request, 'issueForm.html',{'form': form})

@csrf_exempt
def returnBook(request):
    if request.method == "GET":
        books = Book.objects.filter(status = "1")
        return render(request, 'returnForm.html',{'books':books})

    if request.method == "POST":
        bookId = request.POST['bookId']
        book = Book.objects.filter(bookID = bookId)[0]
        book.status = "0"
        book.save()
        return HttpResponseRedirect('/book')
