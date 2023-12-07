import json
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
import pika
from sqlalchemy.orm import sessionmaker
class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:supersenha@localhost:5432/db_loja"
    
    DBBaseModel = declarative_base()
    
    # Configurações RabbitMQ
    RABBITMQ_HOST: str = "localhost"
    RABBITMQ_PORT: int = 5672
    RABBITMQ_USER: str = "admin"
    RABBITMQ_PASSWORD: str = "supersenha"
    RABBITMQ_QUEUE: str = "pagamento"
    
    @property
    def rabbitmq_connection(self):
        credentials = pika.PlainCredentials(self.RABBITMQ_USER, self.RABBITMQ_PASSWORD)
        parameters = pika.ConnectionParameters(
            host=self.RABBITMQ_HOST,
            port=self.RABBITMQ_PORT,
            credentials=credentials
        )
        connection = pika.BlockingConnection(parameters)
        return connection
    
    def send_message_to_queue(self, message_dict):
        with self.rabbitmq_connection as connection:
            channel = connection.channel()
            channel.queue_declare(queue=self.RABBITMQ_QUEUE, durable=True)
            message = json.dumps(message_dict)
            channel.basic_publish(
                exchange='',
                routing_key=self.RABBITMQ_QUEUE,
                body=message,
                properties=pika.BasicProperties(
                    delivery_mode=2,  # make message persistent
                )
            )

    def consume_message_from_queue(self):
        with self.rabbitmq_connection as connection:
            channel = connection.channel()
            channel.queue_declare(queue=self.RABBITMQ_QUEUE, durable=True)

            method_frame, header_frame, body = channel.basic_get(queue=self.RABBITMQ_QUEUE)
            if method_frame:
                try:
                    message_dict = json.loads(body.decode('utf-8'))
                  

                    # Confirma que a mensagem foi processada com sucesso e pode ser removida da fila
                    channel.basic_ack(delivery_tag=method_frame.delivery_tag)

                    return message_dict
                except Exception as e:
                    #
                    print(f"Erro durante o processamento da mensagem: {e}")
                    
                    return None
            else:
                return None

    class Config:
        case_sensitive = True


settings = Settings()



    