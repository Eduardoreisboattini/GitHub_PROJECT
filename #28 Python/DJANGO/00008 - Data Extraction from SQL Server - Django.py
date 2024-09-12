from .models import YourModelName

data = YourModelName.objects.all()
# Or use raw queries:
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM your_table")
    rows = cursor.fetchall()
