from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('^$', views.news, name='news'),
    url('(?P<pk>[0-9]+)/(?P<title>.+)/', views.NewsDetailView.as_view(), name="newsdetail"),
    url('category/(?P<category>.+)/', views.Category.as_view(), name="newscategory"),
    url('addnews/', views.NewsAddView.as_view(), name="addnews"),
    url('update/(?P<pk>[0-9]+)/', views.NewsUpdateView.as_view(), name="updatenews"),
    url('delete/(?P<pk>[0-9]+)/', views.NewsDeleteView.as_view(), name="deletenews"),
]
