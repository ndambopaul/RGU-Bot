from django.db import models

# Create your models here.
class KeyStore(models.Model):
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=500)

    def __str__(self):
        return self.key