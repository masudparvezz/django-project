from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
from crud.forms.allform import *
from crud.models import Category,Product
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

def product(request):
    if request.method=='POST':
        form=ProductForms(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('crud:create_product'))
    else:
        form=ProductForms()
    return render(request, 'crud/create_product.html',{'form':form})

def show_all_product(request):
    value=Product.objects.all()
    return render(request, 'crud/show_all_product.html',{'value':value})

def product_delete(request,pk):
    value=Product.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('crud:create_product'))

def product_edit(request,pk):
    value=Product.objects.all()
    data=Product.objects.get(pk=pk)
    if request.method=='POST':
        form=ProductForms(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('crud:create_product'))
    else:
        form=ProductForms(instance=data)
    return render(request, 'crud/create_product.html',{'form':form})
