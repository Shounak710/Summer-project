from Books import views
from django.conf.urls import url,include

urlpatterns=[
url(r'$', views.BookViewSet.as_view({'get':'list'})),
]
