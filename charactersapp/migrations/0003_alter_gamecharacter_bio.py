# Generated by Django 4.0 on 2022-04-21 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charactersapp', '0002_gamecharacter_fullimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamecharacter',
            name='bio',
            field=models.CharField(max_length=7000),
        ),
    ]