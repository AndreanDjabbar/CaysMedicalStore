# Generated by Django 5.0.2 on 2024-02-16 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_productmodel_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='main/img/product/'),
        ),
    ]