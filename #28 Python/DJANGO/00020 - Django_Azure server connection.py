import polars as pl
import pyodbc

# Azure server connection details
server = 'your_azure_server_name.database.windows.net'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'

# Establish a connection to the Azure server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
)

