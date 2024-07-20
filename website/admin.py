from django.contrib import admin
from .models import Movie, Comment
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_name', 'release_date', 'description')
    list_filter = ('release_date', 'created_at', 'movie_name')
    search_fields = ('movie_name',) 
    ordering = ('movie_name', 'release_date')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user', 'comment', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'movie__movie_name') 
    ordering = ('created_at',)

class UserAdmin(BaseUserAdmin):
    list_display = ('username','date_joined', 'is_staff')
    list_filter = ('date_joined', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username', 'date_joined')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
