from django.db import models

class YourModelName(models.Model):
    column1 = models.CharField(max_length=255)
    column2 = models.IntegerField()
    # Define fields based on your SQL table structure
