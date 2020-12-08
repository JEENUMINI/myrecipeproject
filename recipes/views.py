from django.shortcuts import render,redirect
from recipes.forms import CreateRecipeForm

# Create your views here.

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
    return render(request,"recipes/myrecipes.html")



