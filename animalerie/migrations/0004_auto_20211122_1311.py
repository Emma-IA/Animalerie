# Generated by Django 2.2.24 on 2021-11-22 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animalerie', '0003_delete_billet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='photo',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='equipement',
            name='photo',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]