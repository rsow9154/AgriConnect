from django.db import models

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    crops = models.TextField()

    def __str__(self):
        return self.name