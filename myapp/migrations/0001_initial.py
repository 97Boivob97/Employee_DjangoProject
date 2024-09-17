# Generated by Django 5.1.1 on 2024-09-17 08:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField(default='')),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\d+$', 'Only numeric values are allowed')])),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('designation', models.CharField(max_length=50)),
                ('short_description', models.TextField()),
            ],
        ),
    ]
