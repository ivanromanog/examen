from django.shortcuts import render, redirect
from apps.models import User, Item
# Create your views here.

#validacion
#nombre usuario


def index(request):

    return render(request, 'main.html')

def register(request):
    user = User.objects.register(request.POST)
    request.session['username'] = request.POST['username']
    return redirect('/dashboard')

def login(request):
    user = User.objects.login(request.POST)
    print(User.objects.all())
    request.session['username'] = request.POST['username']
    return redirect('/dashboard')

def dashboard(request):
    id = User.objects.get(username=request.session['username']).id
    name = User.objects.get(username=request.session['username']).name
    context = {
        'user' : request.session['username'],
        'my_items' : Item.objects.filter(creator=id),
        'listed_items' : Item.objects.filter(users=id),
        'others_items' : Item.objects.exclude(creator=id)
    }
    return render(request, 'dashboard.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def addItem(request):

    return render(request, 'create.html')

def createItem(request):
    item = Item.objects.createItem(request.POST, request.session['username'])
    print(Item.objects.all())
    return redirect('/dashboard')

def deleteItem(request, num):
    item = Item.objects.deleteItem(item_id=num)
    return redirect('/dashboard')

def addList(request, num):
    id = User.objects.get(username=request.session['username']).id
    item = Item.objects.get(id=num)
    item.users.add(id)
    return redirect('/dashboard')

def removeList(request, num):
    id = User.objects.get(username=request.session['username']).id
    item = Item.objects.get(id=num)
    item.users.remove(id)
    return redirect('/dashboard')

#La vista de los productos
def itemView(request, num): 
    context = {
        'id' : User.objects.get(username=request.session['username']).id
    }
    return render(request, 'item.html', context)



