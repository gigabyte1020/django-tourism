from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.checks import messages
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from home.forms import SignUpForm, SellSignForm
from guide.models import *


# render home page
def home(request):
    return render(request, 'index.html')


# render discounts page
def discount(request):
    return render(request, 'discount.html')


# render about page
def about(request):
    return render(request, 'about.html')


# render login page
def log(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['id'] = user.id
            role = user.profile.role
            if role == "user":
                # request.session['role'] = user.role
                return redirect('/user/home', {"id": id})
            else:
                return redirect('/guide/home',  {"id": id})
        else:
            return redirect('fail.html')

    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


# render registration page
def reg(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        role = "user"
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.email = form.cleaned_data.get('email')
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.role = "user"
            user.save()
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'reg.html', {'form': form, 'role': 'Users'})


def sellreg(request):
    role = "guide"
    if request.method == 'POST':
        form = SellSignForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.pno = form.cleaned_data.get('pno')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.location = form.cleaned_data.get('location')
            user.profile.role = "guide"
            user.save()
            gd=gdet()
            gd.user=user
            gd.pno = form.cleaned_data.get('pno')
            gd.email = form.cleaned_data.get('email')
            gd.location = form.cleaned_data.get('location')
            gd.save()
            return redirect('/')
    else:
        form = SellSignForm()
    return render(request, 'reg.html', {'form': form, 'role': 'Guides'})
