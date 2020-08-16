from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Usuario'
        verbose_plural_name= 'Usuarios'

    def __str__(self):
        return self.username
