from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    movie_name = models.CharField(max_length=200, verbose_name="Nome do Filme")
    release_date = models.DateField(verbose_name="Data de Lançamento")
    description = models.TextField(verbose_name="Descrição")
    cover_image = models.ImageField(upload_to='movie_covers/', verbose_name="Imagem da Capa")
    watch_links = models.TextField(verbose_name="Links para Assistir", null=True, blank=True)
    trailer_link = models.URLField(verbose_name="Link para o trailer", null=True)

    def __str__(self):
        return self.movie_name

    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"

class Comment(models.Model):
    movie = models.ForeignKey(Movie, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField(verbose_name="Comentário")
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.movie_name} - {self.comment[:20]}"

    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"
