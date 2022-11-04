from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Manager(models.Model):
    CHOICES = [
        ('M','Male'),
        ('F','Female'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    National_ID = models.CharField(max_length=10, null=True)
    Full_Names = models.CharField(max_length=40, null=True)
    Gender = models.CharField(choices=CHOICES, max_length=1, null=True)
    Phone_no = models.CharField(max_length=12, null=True)
    Email = models.EmailField(max_length=100, null=True)
    Bank_name = models.CharField(max_length=25, null=True)
    Account_no = models.CharField(max_length=20, null=True)
    profile_pic = models.ImageField(default='avatar.png', null=True, blank=True)

    # def __str__(self):
    #     self.Full_Names

class Writer(models.Model):
    CHOICES = [
        ('M','Male'),
        ('F','Female'),
    ]
    National_ID = models.CharField(max_length=10, null=True)
    Full_Names = models.CharField(max_length=40, null=True)
    Gender = models.CharField(choices=CHOICES, max_length=1, null=True)
    Phone_no = models.CharField(max_length=12, null=True)
    Email = models.EmailField(max_length=100, null=True)
    Bank_name = models.CharField(max_length=25, null=True)
    Account_no = models.CharField(max_length=20, null=True)

    # def __str__(self):
    #     self.Full_Names

class Order(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)
    writer = models.ForeignKey(Writer, on_delete=models.SET_NULL, null=True)
    order_id = models.CharField(max_length=20, null=True)
    cpp = models.CharField(max_length=10, null=True)
    pages = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

