from re import A
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import widgets
from .models import Blog, Comment
from ckeditor.fields import RichTextField




class PostForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = (
                  "blog_title",
                  "blog_category",
                  "blog_description",
                  "blog_content",
                  'blog_readTime',
                  "header_image"
                  )
        
    blog_title = forms.CharField(max_length=80, widget = forms.TextInput( attrs={'class': 'form-control'}))
    blog_description = forms.CharField(max_length=200, widget= forms.TextInput(attrs={'class': 'form-control'}))
    blog_readTime = forms.CharField(max_length=4, widget= forms.TextInput(attrs={'class': 'form-control'}) )
    header_image = forms.ImageField(required=True)

  
  
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {"body"}
        
        widgets ={
            'body' : forms.Textarea(attrs={'class':'form-control' })
        }
    
    
