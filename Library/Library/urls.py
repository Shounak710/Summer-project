"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from website import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^book/', views.BookViewSet.as_view({'get':'list'})),
    url(r'^user/$', views.UserViewSet.as_view({'get':'list'})),
    url(r'^user/(?P<userId>\w{0,50})/$', views.userRecord),
    url(r'^issueBook',views.issue),
    url(r'^returnBook',views.returnBook),
    url(r'^issuedBook',views.issued.as_view({'get':'list'})),
]
