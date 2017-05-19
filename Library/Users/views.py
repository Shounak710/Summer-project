import django_filters.rest_framework
from rest_framework import generics
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from Users.models import User
from Users.serializers import UserSerializer

# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('ID','User')

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend)
