from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('^$', views.library, name='library'),
    url('(?P<pk>[0-9]+)/(?P<title>.+)/', views.BookDetailView.as_view(), name="bookdetail"),
    url('addbook/', views.BookAddView.as_view(), name="addbook"),

   ]
