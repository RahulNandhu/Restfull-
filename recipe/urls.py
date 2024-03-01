"""
URL configuration for recipe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from shop import views
from search import views as sviews
from rest_framework.authtoken import views as aviews
from rest_framework.routers import SimpleRouter

router=SimpleRouter()
router.register('register',views.U_register)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes',views.recipes.as_view()),
    path('addrecipe/',views.Add_recipe.as_view()),
    path('recipedetails/<int:pk>', views.Recipe_details.as_view()),
    path('recipedelete/<int:pk>', views.Recipe_delete.as_view()),
    path('',include(router.urls)),
    path('login/',aviews.obtain_auth_token),
    path('filter_type/<p>', views.Filter.as_view()),
    path('addreview/<int:pk>', views.Addreview.as_view()),
    path('viewreview/<int:pk>', views.ViewReview.as_view()),
    path('deletereview/<int:pk>', views.DeleteReview.as_view()),
    path('search/', sviews.Search.as_view()),

]
