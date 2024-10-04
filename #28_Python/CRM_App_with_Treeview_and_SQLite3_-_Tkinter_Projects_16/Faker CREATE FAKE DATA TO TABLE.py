# Assistant
from faker import Faker  # Importing Faker for generating fake data
import random  # Importing random for generating random numbers

# Initialize Faker instance
fake = Faker()  # Create an instance of the Faker class to generate fake data

# Number of records you want to create
num_records = 10  # Specify the number of fake records to generate

# Create a list of dictionaries with fake data
data = []  # Initialize an empty list to hold the generated records
for _ in range(num_records):  # Loop to create the specified number of records
    record = {
        "#0": fake.uuid4(),  # Generate a unique identifier (UUID)
        "Novo_GPS": fake.latitude() + ", " + fake.longitude(),  # Generate a fake GPS coordinate
        "#Aliados": random.randint(1000, 9999),  # Generate a random number for "#Aliados"
        "Aliado_ID": random.randint(10000, 99999),  # Generate a random ID for "Aliado_ID"
        "Nome_Aliado": fake.name(),  # Generate a fake name for "Nome_Aliado"
        "Genero": random.choice(['Male', 'Female']),  # Randomly choose a gender
        "Endereco": fake.address(),  # Generate a fake address
        "Bairro": fake.street_name(),  # Generate a fake street name for "Bairro"
        "Cidade": fake.city(),  # Generate a fake city name
        "Uf": fake.state_abbr(),  # Generate a fake state abbreviation
        "Pais": fake.country(),  # Generate a fake country name
        "Cep": fake.postcode(),  # Generate a fake postcode
        "Latitude": fake.latitude(),  # Generate a fake latitude
        "Longitude": fake.longitude(),  # Generate a fake longitude
        "Email": fake.email(),  # Generate a fake email address
        "Data_Compra": fake.date_this_year(),  # Generate a fake purchase date within the current year
        "Origem": fake.company(),  # Generate a fake company name for "Origem"
        "Regiao": random.choice(['Norte', 'Sul', 'Leste', 'Oeste']),  # Randomly choose a region
        "Tipo_Regiao": random.choice(['Rural', 'Urbana']),  # Randomly choose the type of region
        "Micro_Região": fake.city_suffix(),  # Generate a fake suffix for a city
        "#GPS": fake.latitude() + ", " + fake.longitude(),  # Generate another fake GPS coordinate
        "Realizado": random.choice(['Yes', 'No']),  # Randomly choose if the action was completed
        "Dias_GPS": random.randint(1, 365)  # Generate a random number of days for GPS tracking
    }
    data.append(record)  # Append the generated record to the data list

# Output the generated data
for record in data:  # Loop through each record in the data list
    print(record)  # Print the generated record