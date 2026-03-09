FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expõe a porta do Django runserver
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
