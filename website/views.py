from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

def home(request):
    movies = Record.objects.all()


    # ver se o usuário está logado
    if request.method == 'POST':
        username = request.POST['username']
        password= request.POST['password']

        # autenticacao
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login efetuado com sucesso!')
            return redirect('home')
        else:
            messages.success(request, 'Houve um erro ao fazer login, por favor tente novamente...')
            return redirect('home')
    else:
        return render(request, 'home.html', {movies:movies})


def logout_user(request):
    logout(request)
    messages.success(request, 'Você foi deslogado...')
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Você se registrou com sucesso! Bem-vindo!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})
