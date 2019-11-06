from django.db import models

class Director(models.Model):
    films = models.TextField()
    nationality = models.CharField(max_length=100)
    photo_url = models.TextField()
    age = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
