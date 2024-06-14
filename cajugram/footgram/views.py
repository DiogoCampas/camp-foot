from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Record, Publication

def home(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

    # In this we can:
        #Pull data from a database
        #Transform data
        #Send emails

def login_view(request):
    
    records = Record.objects.all() #it will get everything from the table
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html', {'records': records})

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if Record.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        elif Record.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
        else:
            user = Record.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    return render(request, 'registration.html')

@login_required
def user_home(request):
    # Fetch publications from the database (assuming you have a model named 'Publication')
    publications = Publication.objects.all()
    return render(request, 'user_home.html', {'publications': publications})