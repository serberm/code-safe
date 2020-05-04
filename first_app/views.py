from django.shortcuts import render, redirect
from .models import User

SECRET_ANSWER = 'Lady'

# Create your views here.

def dashboard(request):
  return render(request, 'dashboard.html')

def login(request):
  return render(request, 'login.html')

def signup(request):
  return render(request, 'signup.html')

def signup_processing(request):
  name = request.POST['name']
  email = request.POST['email']
  password = request.POST['password']
  secret_question = request.POST['secret_question']

  if secret_question == SECRET_ANSWER:
    new_user = User(
      name=name,
      email = email,
      password = password
      )
    new_user.save()
  else:
    print('wrong secret answer')

  return redirect('/login')

def login_processing(request):
  email = request.POST['email']
  password = request.POST['password']

  user = User.objects.get(email=email)

  if user.password == password:
    return redirect('/dashboard')
  else:
    return redirect('/login')