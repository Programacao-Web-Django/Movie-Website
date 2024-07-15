from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    nome_completo = forms.CharField(label="", max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome Completo'}))
    idade = forms.IntegerField(label="", min_value=16, max_value=130, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Idade'}))

    def clean_idade(self):
        idade = self.cleaned_data.get('idade')
        if idade < 16 or idade > 130:
            raise ValidationError('A idade deve estar entre 16 e 130 anos.')
        return idade

    class Meta:
        model = User
        fields = ('username', 'nome_completo', 'idade', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nome de usuário'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Apenas letras, dígitos e @/./+/-/_.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Sua senha não pode ser muito similar às suas outras informações pessoais.</li><li>Sua senha deve conter pelo menos 8 caracteres.</li><li>Sua senha não pode ser uma senha comum.</li><li>Sua senha não pode ser totalmente numérica.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirme a Senha'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Digite a mesma senha que antes, para verificação.</small></span>'
