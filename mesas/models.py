from django.db import models

class Mesa(models.Model):
    numero = models.PositiveIntegerField(unique=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Mesa {self.numero}"