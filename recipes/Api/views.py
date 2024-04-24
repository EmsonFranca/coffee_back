from rest_framework.viewsets import ModelViewSet
from recipes.models import Recipes, Ingredient
from recipes.Api.serializers import RecipeSerializer, IngredientSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

class RecipeListCreateView(ModelViewSet):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer
    # permission_classes = [IsAuthenticated]

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def create_recipe(request):
        try:
            if request.method == 'POST':
                serializer = RecipeSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save(user=request.user)
                    return Response(serializer.data, status=status.HTTP_200_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)

class IngredientListCreateView(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    # permission_classes = [IsAuthenticated]

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def create_ingredient(request):
        if request.method == 'POST':
            serializer = IngredientSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)