# Generated by Django 3.0.5 on 2020-04-18 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0004_auto_20200418_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(),
        ),
    ]
