# Teste de conhecimentos gerais Python - v2.0- (improved-octo-engine)

## Objetivo

Books Rest API Construa uma API Rest simples em Django, usando Django Rest Framework ou Django Ninja, e um banco de dados Sqlite. Sua API deve conter um CRUD de livros, e cada livro deve ter os seguintes dados cadastrados:

- Ttulo
- ISBN
- Autor(es)
- Editora
- Edição
- Número de páginas
- Descrição rápida

---

## Configurações Iniciais

 1. Tenha certeza de ter o [Python](https://www.python.org/downloads/) Instalado

 2. Crie um [ambiente virtual](https://docs.python.org/3/library/venv.html)

 3. Ative o novo ambiente virtual usando:

> *source "name_used_to_create_venv"/bin/activate*

 4. Instale dentro do novo ambiente virtual criado os pacotes nescessários executando no terminal:

> *pip3 install -r requirements.txt*

---

## Instalação

**Em todos os passos a seguir, sempre que for solicitado algum comando no terminal, e nescessário a ativação do ambiente virtual configurado acima.**

Para subir as tebelas do banco, o django já facilita nossa vida disponibilizando uma ferramemta que mediante os modelos dados, cria arquivos os arquivos para a esse processo. Esses passo já foi efetuado, deixando as configurações de **migrations** prontas. Para subi-las e criar seu próprio DB, utilize o comando:

> *python3 manage.py migrate*

Finalizando a parte de conexão e criação do banco e das tabelas, podemos rodar nossa aplicação e para isso, utiliaremos mais um comando:

> *python3 manage.py runserver*

*Nota-se que agora a API irá continuar rodando até que o usuário solicite o encerramento de suas atividades (ctrl + c).*

---

## Uso

Estamos com nossa API funcionando e pronta para uso, ela está rodando a partir do localhost na porta 8000 - **http://localhost:8000/**, podendo ser acessada de qualquer requisição WEB local.

A API conta com um endpoint **livros**, que da acesso a um crud compelto por requisições, esse endpoint aceita um parametro número que faz referência ao **ID** dos registro. Utilize ele para realizar as ações todas as ações da aplicação que não o READ_ALL

Dentro da API, grças a facilidade do Django, foi criado um controle Admin que pode ser acessado pelo navegador através do endpoint **http://localhost:8000/admin**. Para utiliza-lo você precisa cadastrar um super usuário utilizando o comando:

> *python3 manage.py createsuperuser*

Após isso acesse o link acima e faça o login. Dentro do endpoint "admin" você tambem terá todo controle de todos os campos da API.
