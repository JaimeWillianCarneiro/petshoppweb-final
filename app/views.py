from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import formularioCadastro
def home(request):
    return render(request, 'index.html')

def home2(request):
    return render(request, 'index2.html')


# Create your views here.
def cadastro (request):
    form = formularioCadastro()
    return render(request, 'cadastro.html', {'form': form})


def processaform(request):
    form = formularioCadastro(request.POST)
    if form.is_valid:
        form.save()
        data = {}
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
        return render(request,'cadastro.html',data)


# from .forms import CadastroForm

# def cadastro_view(request):
#     form = CadastroForm()
#     if request.method == 'POST':
#         form = CadastroForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password1']
#             user = User.objects.create_user(username, email, password)
#             user = authenticate(request, username=username, password=password)
#             login(request, user)
#             return redirect('home')
#     return render(request, 'cadastro.html', {'form': form})


def painellogin(request):
    return render(request, 'login.html')





def store(request):
    data = {}
    try:
        usuario_aux = User.objects.get(email=request.POST['email'])
            
        usuario_aux1 = User.objects.get(username=request.POST['username'])

        if usuario_aux or usuario_aux1 :
          
                
            data['msg'] = 'Já existe um usuário com o mesmo e-mail ou como mesmo nome de usuário!'
            data['class'] = 'alert-danger'
                        
    except User.DoesNotExist:
        if(request.POST['password'] != request.POST['password-conf']):
            data['msg'] = 'Senha e confirmação de senha diferentes!'
            data['class'] = 'alert-danger'
        else:
            # print(request.POST['user'])
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            user.first_name = request.POST['name']
            user.last_name = request.POST['sobrenome']
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
        
        return redirect('/home/')
    else:
        print('n existe')
        data['msg'] = 'Usuário ou Senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request,'login.html',data)



def logouts(request):
    logout(request)
    return redirect('/home/')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# from .forms import LoginForm

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/produtos/')
    return render(request, 'login.html', {'form': form})
