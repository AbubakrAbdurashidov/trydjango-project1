# Generated by Django 3.2.21 on 2023-12-16 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_rename_ingredients_ingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
