from django.conf.urls import url, include
from . import views 

urlpatterns = [
    url('^$', views.blog, name='blogs'),
    url('blog/(?P<pk>[0-9]+)/', views.BlogDetailView.as_view(), name="blogdetail"),
    url('addblog/', views.BlogAddView.as_view(), name="addblog"),
    url('^update/(?P<pk>[0-9]+)/(?P<blog_title>.+)/', views.BlogUpdateView.as_view(), name="updateblog"),
    url('^delete/(?P<pk>[0-9]+)/(?P<blog_title>.+)/', views.BlogDeleteView.as_view(), name="deleteblog"),
    url('like/(?P<pk>[0-9]+)/', views.LikeView, name="like"),
    url('comment/(?P<pk>[0-9]+)/', views.CommentView.as_view(), name="comment"),
    
    
    url('category/(?P<blog_category>.+)/', views.Category.as_view(), name="category"),

]
