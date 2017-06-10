from django.db import models

# Create your models here.
class User(models.Model):
    userID = models.AutoField(primary_key=True)
    Name = models.CharField(name='User' , max_length=30)

    def __str__(self):
        return self.User

class Book(models.Model):
    STATUS = (('Issued','Issued'),('Available','Available'))
    bookID = models.AutoField(primary_key=True)
    Name = models.CharField(name='Title' , max_length=30)
    Author = models.CharField(name='Author' , max_length=20)
    Genre = models.CharField(name='Genre' , max_length=10)
    status = models.CharField(max_length=10, choices=STATUS, default="Available")

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
