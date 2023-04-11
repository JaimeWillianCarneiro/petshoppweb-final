from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'index.html')

# Create your views here.
def cadastro (request):
    return render(request, 'cadastro.html')



def painellogin(request):
    return render(request, 'login.html')





def store(request):
    data = {}

    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        print(request.POST['user'])
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request,'cadastro.html',data)



def produtos(request):
    data = {}
    data['user'] = User.objects.get(email =request.user.email)
    
    return render(request, 'produtos.html', data)

def dologin(request):
    data = {}
    print('o que rolou')
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    
    if user is not None:
        print('existe usuario')
        login(request, user)
        
        return redirect('/produtos/')
    else:
        print('n existe')
        data['msg'] = 'Usuário ou Senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request,'login.html',data)



def logouts(request):
    logout(request)
    return redirect('/home/')
