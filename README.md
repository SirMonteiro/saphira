# Saphira API

Bem-vindo ao projeto **Saphira API**, uma API desenvolvida com Django Rest Framework para gerenciar estudantes, palestras, presenças e tokens (e em breve brindes) em um único sistema. A API fornece endpoints para administração e autenticação, bem como para o gerenciamento de dados de estudantes durante a Semana de Sistemas de Informação.

## Índice

- [Recursos](#recursos)
- [Requisitos](#requisitos)
- [Configuração](#configuração)
- [Uso](#uso)
- [Endpoints](#endpoints)

## Recursos

A API Saphira oferece os seguintes recursos:

- **Autenticação**: Login e logout para administradores, login para estudantes.
- **Gerenciamento de Estudantes**: Criação, recuperação, atualização e exclusão de estudantes.
- **Gerenciamento de Presenças**: Registro e recuperação de presenças de estudantes em palestras.
- **Gerenciamento de Palestras**: Criação, recuperação, atualização e exclusão de palestras.
- **Gerenciamento de Tokens**: Criação e listagem de tokens para presenças.
<!-- - **Gerenciamento de Brindes**: Criação, recuperação, atualização e exclusão de brindes. -->

## Requisitos

- Python 3.8+
- Django 4.0+
- Django Rest Framework 3.14+
- Django Rest Framework Simple JWT 5.2+
- Firebase Admin SDK
- PostgreSQL (ou outro banco de dados compatível)

## Configuração

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/SSI-Site/Saphira.git
    cd saphira/src
    ```

2. **Crie um ambiente virtual e ative-o**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. **Instale as dependências**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure o banco de dados**:
- Ajuste as configurações do banco de dados em `settings.py`.

5. **Configure as variáveis de ambiente**:
- Defina as variáveis de ambiente para o Firebase e outras configurações no arquivo `.env`.

6. **Aplique as migrações**:

    ```bash
    python3 manage.py migrate
    ```

7. **Crie um superusuário**:

    ```bash
    python3 manage.py createsuperuser
    ```

8. **Inicie o servidor**:

    ```bash
    python3 manage.py runserver
    ```

## Uso
A API pode ser acessada localmente em `http://localhost:8000/`. Utilize ferramentas como Postman, Insomnia ou cURL para interagir com os endpoints.

### Exemplos de Requisições
**Login do Administrador**:

    ```http
    POST /admin/login
    Content-Type: application/json

    {
      "username": "admin",
      "password": "password123"
    }
    ```
**Login do Estudante**:

    ```http
    POST /student/login
    Content-Type: application/json
    Authorization: Bearer <firebase_token>

    {
      "name": "Alexandre Kira",
      "email": "mesmo.email.firebase@example.com"
    }
    ```

**Criar Presença de Estudante**:

    ```http
    POST /student/{student_id}/presence
    Content-Type: application/json
    Authorization: Bearer <access_token>

    {
      "token_code": "TOKEN1"
    }
    ```

## Endpoints

### Públicos

- `GET /`: Página inicial da API.


- `POST /api/token/refresh`
  - **Descrição**: Atualiza o token JWT de acesso usando um token de refresh válido.
  - **Corpo da Requisição:**
    ```json
    {
      "refresh": "tokenJWTdeRefresh"
    }
    ```

### Estudantes

- `POST /student/login`
  - **Descrição**: Login de estudante.
  - **Cabeçalho**:
    ```
    Authorization: Bearer <firebase_token>
    ```
  - **Corpo da Requisição**:
    ```json
    {
      "name": "Alexandre Kira",
      "email": "mesmo.email.firebase@example.com"
    }
    ```

- `GET /student/{student_id}`
  - **Descrição**: Recupera as informações de um estudante.
  - **Cabeçalho**:
    ```
    Authorization: Bearer <access_token>
    ```

- `PUT /student/{student_id}`
  - **Descrição**: Atualiza as informações de um estudante.
  - **Cabeçalho**:
    ```
    Authorization: Bearer <access_token>
    ```

- `POST /student/{student_id}/presence`
  - **Descrição**: Registra a presença de um estudante em uma palestra.
  - **Cabeçalho**:
    ```
    Authorization: Bearer <access_token>
    ```
  - **Corpo da Requisição**:
    ```json
    {
      "token_code": "TOKEN1"
    }
    ```

- `GET /student/{student_id}/presences`
  - **Cabeçalho**:
    ```
    Authorization: Bearer <access_token>
    ```
  - **Descrição**: Recupera as presenças de um estudante.

### Administradores

- `POST /admin/login`
  - **Descrição**: Login de administrador.
  - **Corpo da Requisição**:
    ```json
    {
      "username": "admin",
      "password": "password123"
    }
    ```

- `POST /admin/logout`
  - **Descrição**: Logout de administrador.

- `GET /admin`
  - **Descrição**: Página inicial para administradores.

- `GET /admin/students`
  - **Descrição**: Lista todos os estudantes.

- `GET /admin/students/search/{name}`
  - **Descrição**: Busca estudantes pelo nome.

- `GET /admin/student/{student_document}`
  - **Descrição**: Recupera informações de um estudante pelo documento.

- `DELETE /admin/students/{student_document}`
  - **Descrição**: Remove um estudante pelo documento.

- `POST /admin/tokens`
  - **Descrição**: Cria um novo token.

- `GET /admin/presences`
  - **Descrição**: Lista todas as presenças.

- `DELETE /admin/presence/{talk_id}/{student_document}`
  - **Descrição**: Remove uma presença específica.
  
  
  
  # AWS
  teste
