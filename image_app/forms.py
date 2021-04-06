from django import forms
from products.models import Product

class productForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'product_img']