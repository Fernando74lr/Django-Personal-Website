from django.db import models

# This class will be represented as a table in the DB.
class Project(models.Model):
    # Every field represents a field in the table.
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)