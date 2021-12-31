from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse
# Create your models here.


class Profile(models.Model):
    # personal
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=600)
    profile_picture= models.ImageField(upload_to="media/profile" )
    telephone = models.CharField(max_length=13, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    work = models.CharField(max_length=70, null=True, blank=True)
    work_address = models.CharField(max_length=100, null=True, blank=True)
    
    # personal links
    whatsapp_number = models.CharField(max_length=100, null=True, blank=True)
    facebook_link = models.CharField(max_length=100, null=True, blank=True)
    twitter_link = models.CharField(max_length=100, null=True, blank=True)
    personal_website_link = models.CharField(max_length=100, null=True, blank=True)
    
    
    # top 3 skills
    skill_one = models.CharField(max_length=50, null=True, blank=True)
    skill_two = models.CharField(max_length=50, null=True, blank=True)
    skill_three = models.CharField(max_length=50, null=True, blank=True)
    
    # highest education
    highest_education = models.CharField(max_length=50, null=True, blank=True)
    programme_majored =  models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return str(self.user)
    

    def get_absolute_url(self):
        """return the blog detail of the immediate blog posted"""
        return reverse('show_profile', args=(str(self.pk)))
    
    



