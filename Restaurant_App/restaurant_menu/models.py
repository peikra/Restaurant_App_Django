from django.db import models

from django.db import models

from user.models import User


# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    cover_photo = models.ImageField(upload_to='restaurant_covers/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='restaurants')

    def __str__(self):
        return self.name


class MainMenuCategory(models.Model):
    name = models.CharField(max_length=50)
    restaurant = models.ForeignKey(Restaurant, related_name='main_categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MenuSubCategory(models.Model):
    name = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='subcategory_covers/')
    parent_category = models.ForeignKey(MainMenuCategory, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='dish_photos/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    subcategory = models.ForeignKey(MenuSubCategory, related_name='dishes', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    dish = models.ManyToManyField(Dish, related_name='ingredients')

    def __str__(self):
        return self.name
