from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

class Department(models.Model):
    depname = models.CharField(max_length=250, unique=True)

class Course(models.Model):
    depid = models.ForeignKey(Department, on_delete=models.CASCADE)
    crsname = models.CharField(max_length=250, unique=True)


class Purpose(models.Model):
    PURPOSE_CHOICES = (
        ('Enquiry', 'For Enquiry'),
        ('Order', 'Place Order'),
        ('Return', 'Return'),
    )
    name = models.CharField(max_length=250, choices=PURPOSE_CHOICES)

    def __str__(self):
        return self.get_name_display()
