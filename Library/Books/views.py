import django_filters.rest_framework
from rest_framework import generics
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from Books.models import Book
from Books.serializers import BookSerializer

# Create your views here.
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('ID','Title', 'Author','Category')

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend)
