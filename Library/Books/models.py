from django.db import models

# Create your models here.
class Book(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(name='Title' , max_length=30)
    Author = models.CharField(name='Author' , max_length=20)
    Category = models.CharField(name='Category' , max_length=10)
    Status = models.IntegerField(name='Status' , default=0 , choices = [(i,i) for i in range(2)])

    def __str__(self):
        return self.Title

    def issueBook(self):
        self.Status = 1
        self.save()

    def returnBook(self):
        self.Status = 0
        self.save()
