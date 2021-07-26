from datetime import datetime
from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    car_id = models.IntegerField()
    customer_need = models.CharField(max_length=200)
    car_title = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    messages = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    create_date = models.DateTimeField(blank=True, default= datetime.now())


    def __str__(self):
        return self.email