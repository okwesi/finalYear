from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('blogs/', include("blog.urls")),
    path('news/', include("news.urls")),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('library/', include('library.urls')),
    
    
    
    
    path('home', views.home, name='home'),
    path('help', views.help, name='help'),
    path('about', views.about, name='about'),
    path('terms', views.terms, name='terms'),
    path('privacy', views.privacy, name='privacy'),
    path('contact', views.contact, name='contact'),

]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
