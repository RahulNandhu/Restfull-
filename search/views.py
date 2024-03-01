from django.shortcuts import render
from shop.models import Recipe
from django.db.models import Q
from rest_framework.views import APIView
from shop.serializers import RecipeSerializers
from rest_framework.response import Response

# Create your views here.



class Search(APIView):
    def get(self,request):
        query=self.request.query_params.get('search') #{query_params:{'search':'values'}}
        if query:
            result=Recipe.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query)| Q(Ingredients__icontains=query))
            p=RecipeSerializers(result,many=True)
            return Response(p.data)

