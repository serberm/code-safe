from django.shortcuts import render, redirect
from .models import User, Card


SECRET_ANSWER = 'Lady'

# Create your views here.

def dashboard(request):
  if not 'logged' in request.session:
    request.session['logged'] = False

  if not request.session['logged']:
    return redirect('/login')
  else:
    context = {
      "all_cards" : Card.objects.all(),
      "user" : User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'dashboard.html', context)

def login(request):
  request.session['logged'] = False
  return render(request, 'login.html')

def signup(request):
  request.session['logged'] = False
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
    request.session['logged'] = True
    request.session['user_id'] = user.id
    return redirect('/dashboard')
  else:
    return redirect('/login')
  
def create(request):
  if not request.session['logged']:
    return redirect('/login')
  else:
    return render(request, 'create.html')

def create_processing(request):
  title = request.POST['title']
  image_url = request.POST['image_url']
  link = request.POST['link']
  content = request.POST['content']

  if not image_url:
    image_url = "Null"
  if not link:
    link = "Null"

  current_user = User.objects.get(id=request.session['user_id'])

  new_post = Card(
    title=title, 
    author = current_user,
    image=image_url, 
    link=link, 
    content=content
    )
  new_post.save()

  return redirect('/dashboard')

def edit(request, id):
  if not request.session['logged']:
    return redirect('/login')
  else:
    context = {
      'card_to_update': Card.objects.get(id=id)
    }
    return render(request, 'edit.html', context)

def edit_processing(request, id):
  title = request.POST['title']
  image_url = request.POST['image_url']
  link = request.POST['link']
  content = request.POST['content']

  if not image_url:
    image_url = "Null"
  if not link:
    link = "Null"

  card_to_update = Card.objects.get(id=id)
  card_to_update.title = title
  card_to_update.image = image_url
  card_to_update.link = link
  card_to_update.content = content

  card_to_update.save()

  return redirect('/dashboard')

def logout(request):
  request.session['logged'] = False
  request.session['user_id'] = 0
  return redirect('login')

def users(request):
  if not request.session['logged']:
    return redirect('/login')
  else:
    context = {
      'all_users': User.objects.all()
    }
    return render(request, 'users.html', context)

  