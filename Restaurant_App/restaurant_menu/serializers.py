from rest_framework import serializers
from .models import Restaurant, MainMenuCategory, MenuSubCategory, Dish, Ingredient

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'phone_number', 'cover_photo']


class MainMenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainMenuCategory
        fields = ['id', 'name', 'restaurant']


class MenuSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuSubCategory
        fields = ['id', 'name', 'cover_image', 'parent_category']


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['id', 'name', 'photo', 'price', 'subcategory']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'dish']
