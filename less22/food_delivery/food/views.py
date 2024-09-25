from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Category
from .forms import CategoryForm

def category(request):
    categories = Category.objects.all()
    return render(request, "category.html", {'categories': categories})


def edit_category(request, c_id):
    if request.method == "GET":
        category = Category.objects.get(pk=c_id)
        print(category)
        cat_form = CategoryForm(instance=category)
        return render(request, "edit_category.html", {'cat_form': cat_form, "id": category.id})
    elif request.method == "POST":
        edited_cat = CategoryForm(request.POST)
        edited_cat.save()
        return redirect("/food/category")


def delete_category(request, c_id):
    category = Category.objects.get(pk=c_id)
    category.delete()
    return redirect("/food/category")


class CreateCategory(ListView):

    def get(self, request):
        cat_form = CategoryForm()
        return render(request, "create_category.html", {'cat_form': cat_form})
    
    def post(self, request):
        cat_form = CategoryForm(request.POST)
        cat_form.save()
        return redirect("/food/category")
