
from django.urls import path
from . import views
app_name = 'crud'
urlpatterns = [
    path('', views.login_page,name="login"),
    path('dashboard', views.dashboard,name="dashboard"),
    path('category/', views.categoryAll,name="category_all"),
    path('category/create', views.categoryView,name="category"),
    path('create_product',views.product,name="create_product"),
    path('product',views.show_all_product,name="show_all_peoduct"),
    path('product_delete/<int:pk>',views.product_delete,name="product_delete"),
    path('product_edit/<int:pk>',views.product_edit,name="product_edit")
]