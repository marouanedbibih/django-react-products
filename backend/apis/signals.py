from django.db.models.signals import post_migrate
from django.dispatch import receiver
from apis.modules.category.models import Category
from apis.modules.product.models import Product

@receiver(post_migrate)
def insert_default_data(sender, **kwargs):
    """
    Insert default categories and products after migrations are run.
    """
    # Create some categories
    categories = [
        {"name": "Electronics", "description": "Devices and gadgets"},
        {"name": "Furniture", "description": "Home and office furniture"},
        {"name": "Clothing", "description": "Apparel and accessories"},
    ]
    
    for category_data in categories:
        category, created = Category.objects.get_or_create(
            name=category_data["name"], 
            defaults={"description": category_data["description"]}
        )
        
        # If the category was created, add products to it
        if created:
            products = [
                {"name": "Laptop", "price": 999.99, "category": category},
                {"name": "Sofa", "price": 499.99, "category": category},
                {"name": "T-Shirt", "price": 19.99, "category": category},
            ]
            for product_data in products:
                Product.objects.get_or_create(
                    name=product_data["name"], 
                    price=product_data["price"], 
                    category=product_data["category"]
                )
