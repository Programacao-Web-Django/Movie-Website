# Generated by Django 5.0.7 on 2024-07-15 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('movie_name', models.CharField(max_length=200, verbose_name='Nome do Filme')),
                ('release_date', models.DateField(verbose_name='Data de Lançamento')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('cover_image', models.ImageField(upload_to='movie_covers/', verbose_name='Imagem da Capa')),
                ('watch_links', models.TextField(help_text='Insira os links separados por vírgula', verbose_name='Links para Assistir')),
            ],
            options={
                'verbose_name': 'Filme',
                'verbose_name_plural': 'Filmes',
            },
        ),
    ]