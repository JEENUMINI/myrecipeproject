"""myrecipeproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path
from recipes.views import create_recipe,list_my_recipes,edit_recipe,view_recipe,delete_recipe,all_recipes,index,start,SearchRecipes

urlpatterns = [

path('create',create_recipe,name="createrecipe"),
path('listrecipe',list_my_recipes,name="listmyrecipes"),
path('edit/<int:id>',edit_recipe,name="edit"),
path('view/<int:id>',view_recipe,name="view"),
path('delete/<int:id>',delete_recipe,name="delete"),
path('allrecipes',all_recipes,name="allrecipes"),
path('index',index,name="index"),
path('start',start,name="start"),
path('search',SearchRecipes,name="search"),

]
