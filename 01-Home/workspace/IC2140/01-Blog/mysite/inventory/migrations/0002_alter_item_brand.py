# Generated by Django 3.2.6 on 2023-12-29 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='brand',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
