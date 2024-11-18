from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    RestaurantViewSet,
    MainMenuCategoryViewSet,
    MenuSubCategoryViewSet,
    DishViewSet,
    IngredientViewSet,
)

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet, basename='restaurant')
router.register(r'categories/main', MainMenuCategoryViewSet, basename='main-category')
router.register(r'categories/sub', MenuSubCategoryViewSet, basename='sub-category')
router.register(r'dishes', DishViewSet, basename='dish')
router.register(r'ingredients', IngredientViewSet, basename='ingredient')

# Include router URLs
urlpatterns = [
    path('', include(router.urls)),
]