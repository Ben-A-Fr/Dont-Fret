# Generated by Django 3.0.5 on 2020-05-12 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DontFretShop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
