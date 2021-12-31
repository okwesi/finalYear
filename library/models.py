from django.db import models
from .validators import validate_file_extension
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Library(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length=300, null=True, blank=True)
    abstract = models.TextField(max_length = 1000)
    E_Book = models.FileField(upload_to="media/library", validators=[validate_file_extension])
    datePosted = models.DateField(("dd mm yyyy"), auto_now_add=True)
    book_cover = models.ImageField(upload_to="media/news" )

    # is_valid = models.BooleanField()
     
    class Meta:
        ordering = ['title']
     
    def __str__(self):
        return f"{self.title} | {self.poster}"
    
    def get_absolute_url(self):
        """return the blog detail of the immediate blog posted"""
        return reverse('bookdetail', args=[self.pk,self.title])