# Generated by Django 3.2.19 on 2023-05-24 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product_name',
        ),
        migrations.AddField(
            model_name='cart',
            name='product_id',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]
