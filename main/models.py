from typing import Iterable
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    stock = models.PositiveIntegerField()
    description = models.CharField(max_length=200)
    product_image = models.ImageField(
        blank=True,
        null=True,
        upload_to="main/img/product/"
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    creator = models.CharField(
        null=True,
        max_length=100
    )
    slug = models.SlugField(blank=True)

    def __str__(self):
        return f"{self.id}. {self.name}"
    
    def save(self):
        self.slug = slugify(self.name)
        super().save()

class ProfileModel(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    name = models.CharField(
        max_length=100,
        null=True
    )
    email = models.EmailField(
        max_length=100,
        null=True
    )
    profile_image = models.ImageField(
        blank=True,
        null=True,
        upload_to="main/img/profile"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        null=True
    )
    updated = models.DateTimeField(
        auto_now=True,
        null=True
    )
    slug = models.SlugField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.id}. {self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)