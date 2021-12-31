from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.

category_choices = [("Coding", "Coding"),("Technology","Technology"), ('Science', 'Science') ]


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_Id = models.AutoField(primary_key=True, auto_created=True)
    blog_title = models.CharField(max_length=80)
    blog_category = models.CharField(choices=category_choices, max_length=20, default="coding")
    blog_description = models.CharField(max_length=200) #uses text field
    blog_content = RichTextField() #use rich text editor here
    blog_readTime = models.IntegerField()
    blog_datePosted = models.DateField(("dd mm yyyy"), auto_now_add=True)
    header_image = models.ImageField(upload_to="media/blogs" )
    likes = models.ManyToManyField(User, related_name='like')
    
    
    @property
    def total_likes(self):        
        return self.likes.count()

    
    def __str__(self):
        """returns the the title and author of the blog in the admin page"""
        return f"{self.blog_title} | {self.author}"
    
    
    def get_absolute_url(self):
        """return the blog detail of the immediate blog posted"""
        return reverse('blogdetail', args=[self.pk,])
        #return reverse('home')
    


class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
    
    def get_absolute_url(self):
        return reverse('blogdetail', kwargs={'pk': self.blog.blog_Id})
    
    def total_comment(self):
        return self.body.count()
    
    
    
    