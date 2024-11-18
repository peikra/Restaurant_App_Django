from rest_framework.viewsets import ModelViewSet
from .models import Restaurant, MainMenuCategory, MenuSubCategory, Dish, Ingredient
from .serializers import (
    RestaurantSerializer,
    MainMenuCategorySerializer,
    MenuSubCategorySerializer,
    DishSerializer,
    IngredientSerializer,
)


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class MainMenuCategoryViewSet(ModelViewSet):
    queryset = MainMenuCategory.objects.all()
    serializer_class = MainMenuCategorySerializer

class MenuSubCategoryViewSet(ModelViewSet):
    queryset = MenuSubCategory.objects.all()
    serializer_class = MenuSubCategorySerializer

class DishViewSet(ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class IngredientViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
