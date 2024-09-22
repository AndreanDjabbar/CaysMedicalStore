from django.contrib import admin
from .models import ProductModel, ProfileModel

class CustomAdmin(admin.ModelAdmin):
    readonly_fields = [
        "created",
        "updated",
        "slug"
    ]


admin.site.register(ProductModel, CustomAdmin)
admin.site.register(ProfileModel, CustomAdmin)