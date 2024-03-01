from django.shortcuts import render
from  .models import Recipe,Review
from .serializers import RecipeSerializers, UserSerializers,ReviewSerializers
from rest_framework.views import APIView
from rest_framework import viewsets,generics,mixins
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.http import Http404

# Create your views here.

class recipes(APIView):
    def get(self,request):
        d=Recipe.objects.all()
        da=RecipeSerializers(d,many=True)
        return Response(da.data)

class Add_recipe(APIView):
    def post(self,request):
        d=RecipeSerializers(data=request.data)
        if d.is_valid():
            d.save()
            return Response(d.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class Recipe_details(mixins.DestroyModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializers

    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

class Recipe_delete(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializers


class U_register(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class Filter(APIView):
    def get(self,request,p):
        d=Recipe.objects.filter(meal_type=p)
        da=RecipeSerializers(d,many=True)
        return Response(da.data,status=status.HTTP_200_OK)

class Addreview(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self,request,pk):
        u = self.request.user
        re=Recipe.objects.get(pk=pk)
        try:
            d=Review.objects.get(user=u,recipe=re)
            msg="You already added a review on this recipe so you can't add new comment until you delete the previous one."
            return Response(msg)
        except:
        # d=ReviewSerializers(data=request.data)
            rat=request.data.get('rating')
            rev=request.data.get('review')
            if (rat >10 or rat <0):
                msg='Rating should be between 0-10'
                return Response(msg)
            else:
                da=Review.objects.create(recipe=re,user=u,rating=rat,review=rev)
                da.save()
                dat=ReviewSerializers(da)
                return Response(dat.data,status=status.HTTP_202_ACCEPTED)


class ViewReview(APIView):
    def get(self,request,pk):
        rec=Recipe.objects.get(pk=pk)
        d=Review.objects.filter(recipe=rec)
        da=ReviewSerializers(d,many=True)
        return Response(da.data,status=status.HTTP_200_OK)

class DeleteReview(APIView):
    def get_details(self,request,pk):
        u=self.request.user
        r=Recipe.objects.get(pk=pk)
        try:
            return Review.objects.get(recipe=r,user=u)
        except:
            raise Http404

    def get(self,request,pk):
        it= self.get_details(request,pk)
        da=ReviewSerializers(it)
        return Response(da.data)

    def delete(self,request,pk):
        it=self.get_details(request,pk)
        it.delete()
        return Response(status=status.HTTP_200_OK)

