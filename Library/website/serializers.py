from rest_framework.serializers import ModelSerializer
from website.models import *

class BookSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class issueSerializer(ModelSerializer):

    class Meta:
        model = issueBook
        fields = '__all__'
