from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
import json

User = get_user_model()

@csrf_exempt
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        services = request.POST.get('services')

        if not email or not name or not password or not password2:
            return render(request, 'signup.html', {'error': 'All fields are required.'})

        if password != password2:
            return render(request, 'signup.html', {'error': 'Passwords do not match.'})

        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'User with this email already exists.'})

        user = User.objects.create_user(email=email, name=name, password=password, services=services)
        return redirect('login')

    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            return render(request, 'signin.html', {'error': 'Invalid email or password'})
    return render(request, 'signin.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def account_view(request):
    return render(request, 'account.html', {
        'name': request.user.name,
        'email': request.user.email,
        'services': request.user.services
        })
