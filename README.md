# Projeto Sensorizador

O **Sensorizador** é uma aplicação web desenvolvida com o framework Django, projetada para o monitoramento e gerenciamento de dados de sensores. A plataforma permite a visualização, cadastro, análise e busca de registros de sensores, além de oferecer uma funcionalidade para importação de dados em massa através de arquivos CSV.
Este projeto centraliza as informações de equipamentos, facilitando a análise e o acompanhamento de métricas importantes em tempo real.

Este projeto está totalmente containerizado usando Docker e Docker Compose, garantindo um ambiente de desenvolvimento consistente e de fácil configuração.

---

## 🚀 Tecnologias Utilizadas

*   **Backend:** Python 3.9, Django, Django REST Framework
*   **Banco de Dados:** PostgreSQL 13
*   **Documentação da API:** Swagger (drf-yasg)
*   **Ambiente:** Docker & Docker Compose

---

## 📋 Pré-requisitos

Antes de começar, garanta que você tenha o [Docker](https://www.docker.com/get-started) e o [Docker Compose](https://docs.docker.com/compose/install/) instalados em sua máquina.

---

## ⚙️ Como Executar o Projeto (Setup)

Siga os passos abaixo para executar a aplicação em seu ambiente de desenvolvimento local.

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/gaelcoder/analise-sensores
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd analise-sensores
    ```

3.  **Construa e inicie os contêineres:**
    Execute o comando abaixo. Ele cuidará de tudo para você:

    ```bash
    docker-compose up --build
    ```

    O que este comando faz:
    *   Constrói a imagem Docker da aplicação Django (usando o `Dockerfile`).
    *   Inicia os contêineres para a aplicação web (`web`) e o banco de dados PostgreSQL (`db`).
    *   Instala todas as dependências do `requirements.txt`.
    *   Aplica automaticamente as migrações do Django (`python manage.py migrate`).
    *   Inicia o servidor de desenvolvimento do Django.

4.  **Acesse a aplicação:**
    Após a inicialização ser concluída (você verá os logs do servidor no terminal), abra seu navegador e acesse:
    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🛠️ Desenvolvimento

Graças à configuração de volumes no `docker-compose.yml`, qualquer alteração feita nos arquivos do projeto (`.py`, `.html`, etc.) na sua máquina local será refletida instantaneamente dentro do contêiner. O servidor de desenvolvimento do Django irá reiniciar automaticamente.

Você **não** precisa reconstruir a imagem (`--build`) para cada mudança no código, apenas quando alterar o `Dockerfile` ou o `requirements.txt`.

---

## ✨ Comandos Úteis do Docker Compose

*   **Parar todos os contêineres:**
    Pressione `Ctrl + C` no terminal onde o compose está rodando, e depois execute:
    ```bash
    docker-compose down
    ```

*   **Parar e remover os dados do banco (use com cuidado!):**
    Este comando irá parar os contêineres e apagar o volume que armazena os dados do PostgreSQL.
    ```bash
    docker-compose down -v
    ```

*   **Executar comandos de gerenciamento do Django:**
    Para executar comandos como `createsuperuser`, `makemigrations`, etc., use `docker-compose exec`:
    ```bash
    # Exemplo para criar um superusuário
    docker-compose exec web python manage.py createsuperuser

    # Exemplo para criar novos arquivos de migração
    docker-compose exec web python manage.py makemigrations
    ```
```