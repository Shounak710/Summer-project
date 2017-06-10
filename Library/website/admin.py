from django.contrib import admin
from website.models import Book,User,issueBook

# Register your models here.
admin.site.register(Book)
admin.site.register(User)
admin.site.register(issueBook)
