from django.contrib import admin
from django.urls import path
from .modules.category.views import CategoryController

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/category/', CategoryController.as_view(), name='category-list'),
    path('api/category/<int:pk>/', CategoryController.as_view(), name='category-detail'),
]
