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

## ✨ Features

*   **Dashboard Interativo:** Visualize os dados dos sensores com paginação para uma navegação fluida.
*   **Busca Inteligente:** Pesquise registros de sensores por ID de equipamento.
*   **Análise de Dados:** Gere médias de leituras de um equipamento específico em diferentes períodos (24h, 48h, 1 semana, 1 mês).
*   **Importação de Dados em Lote:** Envie um arquivo `.csv` para cadastrar múltiplos registros de uma só vez.
*   **API RESTful:** Tenha acesso a um conjunto completo de endpoints para integrar e gerenciar os sensores programaticamente.
*   **Documentação de API:** Explore e teste todos os endpoints através de uma interface Swagger gerada automaticamente.

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
    *   **Interface Web:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    *   **Documentação da API (Swagger):** [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

---

## Endpoints da API

A API RESTful segue os padrões e oferece os seguintes endpoints para o recurso `sensores`:

| Método | Endpoint                | Descrição                                  |
| :----- | :---------------------- | :----------------------------------------- |
| `GET`  | `/api/sensores/`        | Lista todos os registros de sensores.      |
| `POST` | `/api/sensores/`        | Cria um novo registro de sensor.           |
| `GET`  | `/api/sensores/{id}/`   | Retorna um registro de sensor específico.  |
| `PUT`  | `/api/sensores/{id}/`   | Atualiza um registro de sensor.            |
| `PATCH`| `/api/sensores/{id}/`   | Atualiza parcialmente um registro de sensor.|
| `DELETE`| `/api/sensores/{id}/`  | Deleta um registro de sensor.              |

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

## 👨‍💻 Autor

Projeto desenvolvido por **Gabriel Lima de Souza Azevedo**.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gabrielsaz/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/gaelcoder)
