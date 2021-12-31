from re import A
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm
from django import forms
from django.db.models import fields
from django.forms import widgets
from ckeditor.fields import RichTextField

from users.models import Profile


#this field changes the usercreation form from its default and adds the name and email fields to the signup form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget= forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
#the widget changes the default styling to to a bootstrap default form stylings
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


#this functions enables us to change the the default username and password to deafult bootstrap form styling
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'





class EditUserForms(UserChangeForm):
    username = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget= forms.EmailInput(attrs={'class': 'form-control'}))
    
#the widget changes the default styling to to a bootstrap default form stylings
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)





class PasswordChangeForms(PasswordChangeForm):
    old_password = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control'}))

    
#the widget changes the default styling to to a bootstrap default form stylings
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')





class ProfileCreateForm(forms.ModelForm):
    
    
    class Meta:
        model = Profile
        fields  = [ "profile_picture",'bio',
                    "telephone", "address", "work","work_address",
                    "whatsapp_number", "facebook_link", "twitter_link","personal_website_link",
                    "skill_one", "skill_two", "skill_three",
                    "highest_education", "programme_majored"]
        
    
        widgets = {
            'bio' : forms.Textarea(attrs={'class':'form-control bio'}),
            'telephone' : forms.TextInput(attrs={'class':'form-control telephone' }),
            'address' : forms.TextInput(attrs={'class':'form-control address' }),
            'work' : forms.TextInput(attrs={'class':'form-control work' }),
            'work_address' : forms.TextInput(attrs={'class':'form-control work-address' }),
            'whatsapp_number' : forms.TextInput(attrs={'class':'form-control whatsapp' }),
            'facebook_link' : forms.TextInput(attrs={'class':'form-control facebook' }),
            'twitter_link' : forms.TextInput(attrs={'class':'form-control twitter' }),
            'personal_website_link' : forms.TextInput(attrs={'class':'form-control twitter' }),
            'skill_one' : forms.TextInput(attrs={'class':'form-control skill' }),
            'skill_two' : forms.TextInput(attrs={'class':'form-control skill' }),
            'skill_three' : forms.TextInput(attrs={'class':'form-control skill' }),
            'highest_education' : forms.TextInput(attrs={'class':'form-control education' }),
            'programme_majored' : forms.TextInput(attrs={'class':'form-control education' }),
        }
        
        
        
        

           