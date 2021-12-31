from django import forms
from .models import News

class PostForm(forms.ModelForm):

    class Meta:
        model = News
        fields = (
                  "title",
                  "category",
                  "content",
                  "header_image"
                  )
        
    title = forms.CharField(max_length=80, widget = forms.TextInput( attrs={'class': 'form-control'}))
    header_image = forms.ImageField(required=True)


    
    
