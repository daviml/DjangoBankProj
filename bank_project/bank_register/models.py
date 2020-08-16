from django.db import models

# Create your models here.

class Bank(models.Model):
    fullname = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    cod = models.CharField(max_length=3)
    ag = models.CharField(max_length=5)
    cc = models.CharField(max_length=6)