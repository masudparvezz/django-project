from django.forms import ModelForm
from crud.models import Category,Product,Size,ProductSize,ProductImage


class CategoryForms(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class SizeForms(ModelForm):
    class Meta:
        model = Size
        fields = '__all__'


class ProductForms(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ProductSizeForms(ModelForm):
    class Meta:
        model = ProductSize
        fields = '__all__'


class ProductImageForms(ModelForm):
    class Meta:
        model = ProductImage
        fields = '__all__'