from .models import Category
from django.shortcuts import get_object_or_404 # type: ignore

class CategoryService:
    
    @staticmethod
    def create(name, description):
        data = {
            'name': name,
            'description': description
        }
        
        try:
            category = Category.objects.create(**data)
            return True, category
        except Exception as e:
            print(f"Error creating category: {e}")
            return False, None
        
    @staticmethod
    def get_all():
        return Category.objects.all()
    
    @staticmethod
    def get_by_id(id):
        category = get_object_or_404(Category, id=id)
        return category
    
    @staticmethod
    def update(id, name, description):
        try:
            category = get_object_or_404(Category, id=id)
            category.name = name
            category.description = description
            category.save()
            return True, category
        except Exception as e:
            print(f"Error updating category: {e}")
            return False, None
        
    @staticmethod
    def delete(id):
        try:
            category = get_object_or_404(Category, id=id)
            category.delete()
            return True
        except Exception as e:
            print(f"Error deleting category: {e}")
            return False
