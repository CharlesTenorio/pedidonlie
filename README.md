
# Aplicação Pedido Online

**Aluno:** Paulo Cauã

Este é um projeto de aplicação de pedidos online que demonstra o uso de mensageria e programação assíncrona. Utiliza as seguintes ferramentas:

- **Banco de Dados:** PostgreSQL (versão 15)
- **Sistema de Mensageria:** RabbitMQ
- **Linguagem de Programação:** Python (versão 3.12)
- **Framework para Criação de API REST:** FastAPI
- **Objeto Modelo Relacional:** SQLAlchemy

## Pré-requisitos

Para executar a o posgresql e RabbitMQ e aplicação foi criando um Docekrfile e docker-compose.yaml. no Windows, é necessário ter o Docker Desktop instalado. Você pode baixá-lo [aqui](https://www.docker.com/products/docker-desktop/).

## Como Rodar a Aplicação

1. Certifique-se de ter o Docker Desktop instalado.

2. Clone este repositório:

   ```bash
   git clone https://seurepositorio.com/pedido-online.git
   

3. Rodar:
   docker-compose build
   docker-compose up 
   rodar somente o serviço de banco
    docker-compose up dbpostgres_lojaonline

parar todos os serviços
   docker ps -q | ForEach-Object { docker stop $_ }  


## Banco de Dados
   Após a inicialização do serviço é necessário criar um banco     de   dados com o nome "db_loja" e estabelecer a conexão. Para isso, proceda da seguinte forma:

Conecte-se ao banco de dados recém-criado.

Localize o arquivo "001_create_db_pgsql.up.sql" na pasta "migrate" e copie o seu conteúdo.

Execute o script SQL copiado para criar as tabelas necessárias.

Este procedimento garantirá a correta configuração do banco de dados, permitindo o adequado funcionamento do sistema. 

## Instando o ambiente virutal do Python
   1) instala o python 
   2) depois entra no diretorio do projeto e na raiz
   3) python -m venv venv
   4) .\venv\Scripts\activate
   5) pip install -r requirements.txt 
   6) python main.py
   
   ## tudo der certo vai ver essas saida no termnal
   INFO:     Will watch for changes in these directories: []
   INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
   INFO:     Started reloader process [16616] using statreload
   WARNING:  The --reload flag should not be used in production on Windows.
   INFO:     Started server process [3908]
   INFO:     Waiting for application startup.
   INFO:     Application startup complete.
  

 
## Acessar os endpoint 
   http://localhost:8000



   