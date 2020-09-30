from django.db import models



class Inventory(models.Model):
    value_date = models.DateTimeField()
    security = models.CharField(max_length=200)
    currency = models.CharField(max_length=200)
    carry_val = models.IntegerField()
    safekeeping = models.CharField(max_length=200)
    encumberance = models.CharField(max_length=200, choices=[('p', 'Pledged'), ('o', 'Onloan'), ('r', 'Restricted')])

