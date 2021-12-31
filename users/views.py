from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse
from django.views.generic import CreateView
from django.urls.base import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from django.contrib.sites.shortcuts import get_current_site  
from django.template.loader import render_to_string  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  


from users.models import Profile
from . forms import EditUserForms, ProfileCreateForm, SignUpForm, PasswordChangeForms

from django.contrib.auth.models import User  
from django.contrib.auth import get_user_model

from django.utils.encoding import force_bytes, force_text  
from .tokens import account_activation_token  

from django.core.mail import EmailMessage, send_mail 
 
from django.http import HttpResponse 
# Create your views here.



# class UserSignUp(CreateView):
#     """Creates forms and allows user to register as a user"""
#     form_class = SignUpForm
#     template_name = 'registration/signup.html'
#     success_url = reverse_lazy('login')



class UpdateUserDetails(UpdateView):
    """creates forms and allow users to update their details"""
    form_class = EditUserForms

    template_name = 'users/updateuser.html'
    success_url = reverse_lazy('blogs')

    def get_object(self):
        return self.request.user


class PasswordChange(PasswordChangeView):
    """class for creating forms for users to change their passwords....
    currently not in use since this class is also provided by the allauth model"""
    form_class = PasswordChangeForms
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('edit_usersettings')
    
    

class CreateProfileView(CreateView):
    """class is used to create a profile for a new user"""
    model = Profile 
    template_name = "users/create_profile.html"
    form_class = ProfileCreateForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
   
   
   
    
    
class ShowProfileView(DetailView):
    """show the profile of blogger from the bog detail"""
    model = Profile
    template_name = 'users/profile.html'

    
    
    def  get_context_data(self, **kwargs):

        context = super(ShowProfileView, self).get_context_data(**kwargs)
        
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context
    

def sendMail(request, **kwargs):
    pk = kwargs['pk']
    profile = get_object_or_404(Profile, pk=pk)
    user_email = profile.user.email
    print(profile, user_email, pk)
    if request.method == "POST":
        message =  request.POST['message']
        name = request.POST['name']
        subject1 = request.POST['subject']
        email = request.POST['email']
        subject = (f"Hi, you got a mail from {name} {email}. Subject: {subject1}")
        send_mail(
        subject,
        message,       
        email,
        [user_email],
        fail_silently=False,
        )   

    return HttpResponseRedirect(reverse('show_profile', args=[str(pk),]))
    

class EditProfileView(UpdateView):
    """class for creating forms for users to edit their profiles """
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'users/edit_profile.html'
    # fields = ["bio","profile_picture", "telephone", "address", "work", ]
    
    
 


def signup(request):  
    """function for creating forms to add users then sends a verification link to the email of the user"""
    if request.method == 'POST':  
        form = SignUpForm(request.POST)  
        if form.is_valid():  
            # save form in the memory not in database  
            user = form.save(commit=False)  
            user.is_active = False  
            user.save()  
            # to get the domain of the current site  
            current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('users/acc_active_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()  
            return render(request, 'users/activate_email.html', {})
    else:  
        form = SignUpForm()  
    return render(request, 'registration/signup.html', {'form': form})  




def activate(request, uidb64, token): 
    """function that activates the users account when they
    click on the activation link sent to their email""" 
    User = get_user_model()  
    try:  
        uid = force_text(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return render(request, 'users/activate_success.html', {})  
    else:  
        return HttpResponse('Activation link is invalid!')  