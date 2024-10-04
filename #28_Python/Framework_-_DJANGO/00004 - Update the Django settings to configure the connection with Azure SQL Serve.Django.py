DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': '<your-database-name>',
        'USER': '<your-username>',
        'PASSWORD': '<your-password>',
        'HOST': '<your-server-name>.database.windows.net',
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'extra_params': 'TrustServerCertificate=yes;'
        },
    }
}
