# Generated by Django 2.2.5 on 2019-10-22 22:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empleados', '0003_auto_20191022_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='salario',
            field=models.DecimalField(decimal_places=2, max_digits=2, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Salario (Mensual)'),
        ),
    ]
