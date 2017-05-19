from Users import views
from django.conf.urls import url,include

urlpatterns=[
url(r'$', views.UserViewSet.as_view({'get':'list'})),
]
