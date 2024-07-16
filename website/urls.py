from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_user, name='logout'), 
    path('register/', views.register_user, name='register'),
    path('<int:id>', views.movie, name='movie'),
    path('<int:id>/comment/', views.comment_movie, name='comment_movie'),
]
