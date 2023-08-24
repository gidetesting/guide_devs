from django.db import models

# Create your models here.
class info(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=1000)
    def __str__(self):
        return self.name

class basic(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    subject = models.CharField(max_length=1000)
    def __str__(self):
        return self.name

class intermediate(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    subject = models.CharField(max_length=1000)
    def __str__(self):
        return self.name

class premium(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    subject = models.CharField(max_length=1000)
    def __str__(self):
        return self.name
    