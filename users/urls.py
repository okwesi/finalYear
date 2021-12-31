from django.conf.urls import url, include
from django.urls.conf import path
from . views import CreateProfileView, EditProfileView, ShowProfileView, UpdateUserDetails, PasswordChange, sendMail, signup,activate
from django.contrib.auth import views as auth_views



urlpatterns = [    
        # url('signup/', UserSignUp.as_view(), name='signup'),
        url('signup/', signup, name='signup'),
        path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  activate, name='activate'),  
        url('edit-usersettings/', UpdateUserDetails.as_view(), name='edit-usersettings'),
        url('accounts/', include('django.contrib.auth.urls')),
        path('accounts/', include('allauth.urls')),
        
        url('(?P<pk>[0-9]+)/createprofile/', CreateProfileView.as_view(), name="create_profile"),
        url('(?P<pk>[0-9]+)/profile/', ShowProfileView.as_view(), name="show_profile"),
        url('(?P<pk>[0-9]+)/editprofile/', EditProfileView.as_view(), name="edit_profile"),

        path('accounts/', include('social_django.urls', namespace='social')), 
        
        url('(?P<pk>[0-9]+)/send/', sendMail, name="send"),


]
