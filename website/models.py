from django.db import models


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    movie_name = models.CharField(max_length=200, verbose_name="Nome do Filme")
    release_date = models.DateField(verbose_name="Data de Lançamento")
    description = models.TextField(verbose_name="Descrição")
    cover_image = models.ImageField(upload_to='movie_covers/', verbose_name="Imagem da Capa")
    watch_links = models.TextField(verbose_name="Links para Assistir", help_text="Insira os links separados por vírgula")

    def __str__(self):
        return self.movie_name

    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"

