from django import forms
from .models import Library

class PostForm(forms.ModelForm):

    class Meta:
        model = Library
        fields = (
                  "title",
                  "author",
                  "abstract",
                  "book_cover",
                  "E_Book"
                  )
        
    title = forms.CharField(max_length=80, widget = forms.TextInput( attrs={'class': 'form-control'}))
    author = forms.CharField(max_length=300, widget = forms.TextInput( attrs={'class': 'form-control'}))
    abstract = forms.CharField(max_length=1000, widget = forms.Textarea( attrs={'class': 'form-control'}))
    book_cover = forms.ImageField(required=True)


    
    
