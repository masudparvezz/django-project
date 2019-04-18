from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login_page(request):
    return render(request,'crud/login.html')

def crud(request):
    return render(request,'crud/admin_home.html')