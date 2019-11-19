from django.db import models

# Create your models here.

class Sector(models.Model):
    user_name = models.CharField(max_length=30)

    def __str__(self):
        return self.user_name