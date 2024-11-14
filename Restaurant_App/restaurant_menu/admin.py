from django.contrib import admin

from restaurant_menu.models import Restaurant, MainMenuCategory,MenuSubCategory,Dish,Ingredient



# Register your models here.
admin.site.register(Restaurant)
admin.site.register(MainMenuCategory)
admin.site.register(MenuSubCategory)
admin.site.register(Dish)
admin.site.register(Ingredient)