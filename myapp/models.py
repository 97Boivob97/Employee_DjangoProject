from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(default="")
    phone_number = models.CharField(max_length=15,validators=[RegexValidator(r'^\d+$', 'Only numeric values are allowed')])
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    designation = models.CharField(max_length=50)
    short_description = models.TextField()



