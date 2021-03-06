from django.shortcuts import render,redirect
from recipes.forms import CreateRecipeForm
from recipes.models import Recipe
from django.contrib.auth.decorators import login_required
from recipes.filters import RecipeFilter

# Create your views here.
def index(request):
    return render(request,"recipes/index.html")

def start(request):
    return render(request,"recipes/start.html")

def create_recipe(request):
    form=CreateRecipeForm(initial={"created_by":request.user})
    context={}
    context["form"]=form
    if request.method=='POST':
        form=CreateRecipeForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listmyrecipes")
        else:
            context["form"]=form
            return render(request,"recipes/createrecipe.html",context)
    return render(request,"recipes/createrecipe.html",context)

def list_my_recipes(request):
    my_recipes=Recipe.objects.filter(created_by=request.user)
    context={}
    context["recipes"]=my_recipes
    return render(request,"recipes/myrecipes.html",context)

def edit_recipe(request,id):
    recipe=Recipe.objects.get(id=id)
    form=CreateRecipeForm(instance=recipe)
    context={}
    context["form"]=form
    if request.method=='POST':
        form=CreateRecipeForm(instance=recipe,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listmyrecipes")
        else:
            context["form"]=form
            return render(request,"recipes/editrecipe.html",context)
    return render(request,"recipes/editrecipe.html",context)

def view_recipe(request,id):
    recipe=Recipe.objects.get(id=id)
    context={}
    context["recipe"]=recipe
    return render(request,"recipes/recipeview.html",context)

def delete_recipe(request,id):
    Recipe.objects.get(id=id).delete()
    return redirect("listrecipes")

@login_required
def all_recipes(request):
    recipes=Recipe.objects.all()
    context={}
    context["recipes"]=recipes
    return render(request,"recipes/allrecipes.html",context)


def SearchRecipes(request):
    recipes=Recipe.objects.all()
    myfilter=RecipeFilter(request.GET,queryset=recipes)
    recipes=myfilter.qs
    context={}
    context["recipes"]=recipes
    context["myfilter"]=myfilter
    return render(request,"recipes/recipe_search.html",context)




