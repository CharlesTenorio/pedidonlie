# Use a imagem oficial do Python como base
FROM python:3.12

# Define o diretório de trabalho como /app
WORKDIR /app

# Copia o arquivo requirements.txt para o contêiner no diretório /app
COPY requirements.txt .

# Instala as dependências listadas no requirements.txt
RUN python -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Copia todo o conteúdo do diretório atual para o contêiner no diretório /app
COPY . .

# Expõe a porta 8000
EXPOSE 8000

# Comando para iniciar a aplicação usando uvicorn
CMD ["./venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]