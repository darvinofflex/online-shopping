from django import forms

from . models import Category, Product, User


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields =('name', 'slug')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =('name', 'slug', 'cover', 'description', 'price', 'available')


class UserForm(forms.ModelForm):
     password = forms.CharField(widget=forms.PasswordInput)

     class meta:
         model = User
         fields =('username', 'email', 'password')

