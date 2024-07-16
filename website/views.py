from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib import messages
from .forms import SignUpForm, CommentForm
from .models import Movie

def home(request):
    if request.user.is_authenticated:
        movies = Movie.objects.all()
        context = {'movies': movies}
        return render(request, 'home.html', context)
    else:
        return redirect('login')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Credenciais inválidas'})
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'Você foi deslogado...')
    return redirect('login')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			auth_login(request, user)
			messages.success(request, "Você se registrou com sucesso! Bem-vindo!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def movie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    watch_links = movie.watch_links.split(',') if movie.watch_links else []
    context = comment_movie(request,id)
    context['watch_links'] = watch_links
    return render(request, 'movie.html', context)

def comment_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()

            return redirect('movie', id=movie.id)
    else:
        comment_form = CommentForm()
    return {'comment_form': comment_form, 'movie': movie}

