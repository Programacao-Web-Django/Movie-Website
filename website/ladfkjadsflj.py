# class Movie
    # @property
    # def average_rating(self):
    #     ratings = self.rates.all()
    #     if ratings:
    #         total_ratings = sum([rating.value for rating in ratings])
    #         return total_ratings / len(ratings)
    #     else:
    #         return 0
# 
#  class Rate(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='rates', verbose_name="Filme")
#     value = models.IntegerField(verbose_name="Avaliação", default=0, help_text="Insira uma avaliação de 1 a 5")
#     created_at = models.DateTimeField(auto_now_add=True, null=True)

#     class Meta:
#         unique_together = ('user', 'movie')  # Define que um usuário só pode avaliar um filme uma vez
#         verbose_name = "Avaliação"
#         verbose_name_plural = "Avaliações"

# class RateForm(forms.ModelForm):
#     value = forms.ChoiceField(
#         label="Sua Avaliação",
#         choices=[(i, str(i)) for i in range(1, 6)],
#         widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
#     )

#     class Meta:
#         model = Rate
#         fields = ['value']

#     def __init__(self, *args, **kwargs):
#         super(RateForm, self).__init__(*args, **kwargs)
#         self.fields['value'].help_text = '<span class="form-text text-muted"><small>Escolha uma nota de 1 a 5.</small></span>'

# {{rate_form.value.label_tag}}
#         {%for radio in rate_form.value%}
#         <span class="form-group">
#             {{ radio }}
#         </span>
#         {% endfor %} <br/><br/>

# <h3>Avaliações:</h3>
#     {% for rate in movie.rates.all %}
#         <div class="card my-2">
#             <div class="card-body">
#                 <h5 class="card-title">{{ rate.user.username }}</h5>
#                 <p class="card-text">Nota: {{ rate.value }} estrelas</p>
#                 <p class="card-text"><small class="text-muted">Avaliado em: {{ rate.created_at }}</small></p>
#             </div>
#         </div>
#     {% endfor %}

# def rate_movie(request, id):
#         # rate_form = RateForm(request.POST)
#         if rate_movie.is_valid():
#               rate = rate_form.save(commit=False)
#             rate.movie = movie
#             rate.user = request.user
#             rate.save()
#         else:
#             rate_form = RateForm()
#     return {'rate_form': rate_form}

#  <!-- <li class="nav-item dropdown">
#             <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
#             Categorias
#           </a>
#           <ul class="dropdown-menu">
#             <li><a class="dropdown-item" href="#">Action</a></li>
#             <li><a class="dropdown-item" href="#">Another action</a></li>
#             <li><hr class="dropdown-divider"></li>
#             <li><a class="dropdown-item" href="#">Something else here</a></li>
#           </ul>
#         </li>