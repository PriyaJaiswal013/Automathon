from django.db import models
from django.contrib.auth.models import User
from customer.models import Customer
from datetime import date
class Category(models.Model):
    category_name =models.CharField(max_length=20)
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.category_name

class Policy(models.Model):
    category= models.ForeignKey('Category', on_delete=models.CASCADE, default='Health Insurance')
    policy_name=models.CharField(max_length=200)
    sum_assurance=models.PositiveIntegerField(default=500000)
    Pateint_name=models.CharField(max_length=500)
    contact_no=models.IntegerField(default='')
    gender=models.CharField(max_length=200)
    # date_of_birth=models.DateField(null = True)
    insured_card_id_number=models.CharField(max_length=500)
    total_cost_hospitalization=models.PositiveIntegerField()
    creation_date =models.DateField(auto_now=True)
    status = models.CharField(max_length=100,default='Pending')

    def __str__(self):
        return self.policy_name


class Question(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    description =models.CharField(max_length=500)
    admin_comment=models.CharField(max_length=200,default='Nothing')
    asked_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.description