from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=50)

class Meal(models.Model):
    meal_name = models.CharField(max_length=50, unique=True)


class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_desc = models.CharField(max_length=200)
    item_category = models.ManyToManyField(Meal)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField(default="item_pic.jpg", upload_to="item")
