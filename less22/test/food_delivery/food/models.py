from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class FDUser(User):
    role = models.CharField(max_length=30)


class Category(models.Model):
    name = models.CharField(max_length=255)


class Food(models.Model):
    name = models.CharField(max_length=255)
    cost = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Order(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders")
    courier = models.ForeignKey(
        FDUser, on_delete=models.CASCADE, related_name="to_order")


def __str__(self):
    return f"{self.id}-{self.adress}"
