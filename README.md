# Django Movie Website

Este é um projeto de um website de filmes desenvolvido com Django. O objetivo deste projeto é permitir que os usuários visualizem uma lista de filmes, e comentem sobre os filmes. Cada filme possui informações detalhadas como nome, data de lançamento, descrição, imagem da capa, links para assistir e trailer.

## Autor

  - Saimon Gabriel de Andrade

## Funcionalidades

1. **Visualização de Filmes**:
   - Listagem de filmes com detalhes como nome, data de lançamento, descrição, imagem da capa, links para assistir e trailer.

2. **Autenticação de Usuário**:
   - Registro de novos usuários.
   - Login e logout de usuários.

3. **Comentários**:
   - Usuários podem comentar sobre os filmes.

## Instalação

### Pré-requisitos

- Python 3.x
- MySQL
- Django 3.x

### Passos

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu-usuario/django-movie-website.git
   cd django-movie-website
   ```

2. **Instale as dependências**

   
3. **Configuração do Banco de Dados**:

   Configure o banco de dados MySQL no arquivo `settings.py`:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'base',
           'USER': 'root',
           'PASSWORD': '8844',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

4. **Migre o banco de dados**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crie um superusuário**:

   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor de desenvolvimento**:

   ```bash
   python manage.py runserver
   ```

7. **Acesse o site**:

   Abra o navegador e acesse `http://127.0.0.1:8000`.

## Estrutura do Projeto

- **models.py**: Define os modelos do banco de dados, incluindo Movie, Rate e Comment.
- **views.py**: Define as views que lidam com as requisições e retornam respostas.
- **forms.py**: Define os formulários utilizados para registro de usuários, avaliações e comentários.
- **urls.py**: Define as rotas do projeto.
- **templates/**: Contém os templates HTML usados para renderizar as páginas.

---
