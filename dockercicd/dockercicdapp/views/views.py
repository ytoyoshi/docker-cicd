from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView
from ..forms import LoginForm
from ..models import Page

class login_view(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True

    form_class = LoginForm

@login_required
def home_view(request):
    pages = Page.objects.filter(show_on_home = True)
    return render(request, 'home.html', {'pages': pages})

@login_required
def logout_user(request):
    logout(request)
    return render(request, 'logout_confirmation.html')

@login_required
def logout_confirmation_view(request):
    # print("logout ")
    return render(request, 'logout_confirmation.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


