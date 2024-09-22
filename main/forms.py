from django import forms
from .models import ProductModel, ProfileModel

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = [
            "name",
            "stock",
            "description",
            "product_image"
        ]
        widgets = {
            "name":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Input Product's Name"
                }
            ),
            "stock":forms.NumberInput(
                attrs={
                    "class":"form-control",
                }
            ),
            "description":forms.Textarea(
                attrs={
                    "class":"form-control",
                    "placeholder":"Input Description"
                }
            ),
            "product_image":forms.FileInput(
                attrs={
                    "class":"form-control-file"
                }
            )
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = [
            "name",
            "email",
            "profile_image"
        ]
        widgets = {
            "name":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Input Your Name"
                }
            ),
            "email":forms.EmailInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Input Your Email"
                }
            ),
            "profile_image":forms.FileInput(
                attrs={
                    "class":"form-control-file"
                }
            )
        }