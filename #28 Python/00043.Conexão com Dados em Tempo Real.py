from kafka import KafkaConsumer
import pandas as pd

# Configuração do Kafka Consumer
consumer = KafkaConsumer('nome-do-topico', bootstrap_servers='localhost:9092')

# Processamento das mensagens
data = []
for message in consumer:
    # Processando cada mensagem recebida
    data.append(message.value.decode('utf-8'))
    if len(data) >= 100:  # Armazena 100 mensagens de cada vez
        df = pd.DataFrame(data)
        print(df.head())
        data = []
