
from django.urls import path
from . import views
app_name = 'crud'
urlpatterns = [
    path('', views.login_page,name="login"),
    path('dashboard', views.dashboard,name="dashboard"),
    path('category/', views.categoryAll,name="category_all"),
    path('category/create', views.categoryView,name="category"),
]