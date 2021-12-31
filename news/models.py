from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.

category_choices = [("Local", "Local"),("World","World"), ('Campus', 'Campus')]


class News(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    category = models.CharField(choices=category_choices, max_length=20)
    content = RichTextField() #use rich text editor here
    datePosted = models.DateField(("dd mm yyyy"), auto_now_add=True)
    header_image = models.ImageField(upload_to="media/news" )   
    
  
    
    def __str__(self):
        """returns the the title and author of the blog in the admin page"""
        return f"{self.title} | {self.reporter}"
    
    
    def get_absolute_url(self):
        """return the blog detail of the immediate blog posted"""
        return reverse('newsdetail', args=[self.pk,self.title])
    #     #return reverse('home')
    
