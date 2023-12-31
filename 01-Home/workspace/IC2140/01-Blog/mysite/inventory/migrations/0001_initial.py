# Generated by Django 3.2.6 on 2023-12-29 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_no', models.CharField(max_length=8)),
                ('loc', models.CharField(max_length=5)),
                ('owner', models.CharField(max_length=20)),
                ('desc', models.TextField()),
                ('brand', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('purchase_date', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'items',
            },
        ),
    ]
