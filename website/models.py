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

    @property
    def average_rating(self):
        ratings = self.rates.all()
        if ratings:
            total_ratings = sum([rating.value for rating in ratings])
            return total_ratings / len(ratings)
        else:
            return 0

    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"

class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='rates', verbose_name="Filme")
    value = models.IntegerField(verbose_name="Avaliação", default=0, help_text="Insira uma avaliação de 1 a 5")

    class Meta:
        unique_together = ('user', 'movie')  # Define que um usuário só pode avaliar um filme uma vez
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
