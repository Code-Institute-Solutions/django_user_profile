from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.urlresolvers import reverse


# Create your views here.
def index(request):
    return render(request, "index.html")
    
    
def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))
