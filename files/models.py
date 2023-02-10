from django.db import models

class File(models.Model):
    upload = models.FileField(upload_to="uploads/", max_length=267)

class Store(models.Model):
    type = models.CharField(max_length=120)
    date = models.DateField(max_length=120)
    value = models.IntegerField(max_length=120)
    cpf = models.IntegerField(max_length=120)
    card = models.IntegerField(max_length=120)
    hour = models.TimeField(max_length=120)
    owner = models.CharField(max_length=120)
    store = models.CharField(max_length=120)