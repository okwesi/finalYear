from django.shortcuts import get_object_or_404, redirect, render

def home(request):
    return render(request, 'home.html')

def help(request):
    return render(request, 'footer/help.html')

def about(request):
    return render(request, 'footer/about-us.html')

def terms(request):
    return render(request, 'footer/terms.html')

def privacy(request):
    return render(request, 'footer/privacy.html')

def contact(request):
    return render(request, 'footer/contact.html')

