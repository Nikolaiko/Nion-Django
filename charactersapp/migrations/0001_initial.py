# Generated by Django 3.2.9 on 2022-03-20 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameCharacter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('characterName', models.CharField(max_length=20)),
                ('damage', models.IntegerField()),
                ('health', models.IntegerField()),
                ('avatar', models.ImageField(blank=True, upload_to='')),
                ('bio', models.CharField(max_length=70)),
            ],
        ),
    ]
