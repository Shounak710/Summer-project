from django.db import models

# Create your models here.
class User(models.Model):
    ID = models.AutoField(primary_key=True)
    userID = models.CharField(max_length=10 , default = " ")
    Name = models.CharField(name='User' , max_length=30)

    def __str__(self):
        return self.User

class Book(models.Model):
    STATUS = (('1','1'),('0','0'))
    ID = models.AutoField(primary_key=True)
    bookID = models.CharField(max_length=10, default = " ")
    Name = models.CharField(name='Title' , max_length=30)
    Author = models.CharField(name='Author' , max_length=20)
    Genre = models.CharField(name='Genre' , max_length=10)
    status = models.CharField(max_length=10, choices=STATUS, default="0")

    def __str__(self):
        return self.Title

class issueBook(models.Model):
    book = models.ForeignKey('Book', name = 'Book')
    libraryUser = models.ForeignKey('User')
    issueTime = models.DateTimeField(auto_now=True)
    noOfDays = models.IntegerField(default=0)
    fine = models.IntegerField(default = 0)

    def __str__(self):
        return self.Book.Title
