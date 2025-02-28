from django.shortcuts import render 
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from .service import CategoryService
from .serializer import CategorySerializer

class CategoryController(APIView):
    # Fetch all categories or a specific category
    def get(self,request,pk=None):
        if pk:
            try:
                category = CategoryService.get_by_id(pk)
                serializer = CategorySerializer(category)
                return Response(serializer.data,status=status.HTTP_200_OK)
            except Exception as e:
                print(f"Error getting category: {e}")
                return Response({"message": "Error fetching this category"}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                categories = CategoryService.get_all()
                serializer = CategorySerializer(categories, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                print(f"Error getting categories: {e}")
                return Response({"message": "Error fetching categories"}, status=status.HTTP_404_NOT_FOUND)
            
    # Create a new category
    def post(self, request):
        data = request.data
        name = data.get('name')
        description = data.get('description')
        success, category = CategoryService.create(name, description)
        if success:
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Error creating category"}, status=status.HTTP_400_BAD_REQUEST)
        
    # Update a category
    def put(self, request, pk):
        data = request.data
        name = data.get('name')
        description = data.get('description')
        success, category = CategoryService.update(pk, name, description)
        if success:
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Error updating category"}, status=status.HTTP_400_BAD_REQUEST)
        
    # Delete a category
    def delete(self, request, pk):
        success = CategoryService.delete(pk)
        if success:
            return Response({"message": "Category deleted"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Error deleting category"}, status=status.HTTP_400_BAD_REQUEST)
            
        
        
        