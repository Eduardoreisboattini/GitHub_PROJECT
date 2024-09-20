from faker import Faker
import random

# Initialize Faker instance
fake = Faker()

# Number of records you want to create
num_records = 10

# Create a list of dictionaries with fake data
data = []
for _ in range(num_records):
    record = {
        "#0": fake.uuid4(),
        "Novo_GPS": f"{fake.latitude()},{fake.longitude()}",
        "#Aliados": random.randint(1000, 9999),
        "Aliado_ID": random.randint(10000, 99999),
        "Nome_Aliado": fake.name(),
        "Genero": random.choice(['Male', 'Female']),
        "Endereco": fake.address(),
        "Bairro": fake.street_name(),
        "Cidade": fake.city(),
        "Uf": fake.state_abbr(),
        "Pais": fake.country(),
        "Cep": fake.postcode(),
        "Latitude": fake.latitude(),
        "Longitude": fake.longitude(),
        "Email": fake.email(),
        "Data_Compra": fake.date_this_year(),
        "Origem": fake.company(),
        "Regiao": random.choice(['Norte', 'Sul', 'Leste', 'Oeste']),
        "Tipo_Regiao": random.choice(['Rural', 'Urbana']),
        "Micro_Região": fake.city_suffix(),
        "#GPS": f"{fake.latitude()},{fake.longitude()}",
        "Realizado": random.choice(['Yes', 'No']),
        "Dias_GPS": random.randint(1, 365)
    }
    data.append(record)

# Output the generated data
for record in data:
    print(record)
