from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
from crud.forms.allform import *
from crud.models import *
# Create your views here.
def login_page(request):
    return render(request,'crud/login.html')

def dashboard(request):
    return render(request,'crud/admin_home.html')

def categoryView(request):
    if request.method == 'POST':
        form = CategoryForms(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('crud:category'))

    if request.method == 'GET':
        form = CategoryForms()
        context = {
            'form':form
        }
        return render(request, 'crud/create_category.html',context)

def categoryAll(request):
    if request.method == 'GET':
        allcategory = Category.objects.all()
        context = {
            'allcategory':allcategory
        }
        return render(request, 'crud/category_show.html',context)