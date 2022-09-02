from django.db import models
class Size(models.Model):
    SIZE = [
        ("1" , "small"),
        ("2" , "medium"),
        ("3" , "large"),
    ]
    size = models.CharField(max_length=1, choices=SIZE)

class Pizza(models.Model):
    topping1 = models.CharField("Topping_1", max_length=50)
    topping2 = models.CharField("Topping_2", max_length=50)
    size = models.OneToOneField(Size, on_delete=models.CASCADE)