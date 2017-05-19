from django.db import models

# Create your models here.
class User(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(name='User' , max_length=30)

    def __str__(self):
        return self.Title
