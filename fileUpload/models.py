from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    date_of_birth = models.DateField()

class Finance(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    month = models.CharField(max_length = 100)
    income = models.CharField(max_length = 100)