from enum import unique
from django.db import models

# Create your models here.
class Info(models.Model):
    nome = models.CharField(max_length = 100, blank=True, null=True)
    e_mail = models.EmailField(max_length = 50, unique = True, blank=True, null=True)
    content = models.TextField(max_length = 500, blank=True, null=True)
    date = models.DateTimeField(auto_now_add = True, blank=True, null=True)

    def __str__(self):
        return self.nome
