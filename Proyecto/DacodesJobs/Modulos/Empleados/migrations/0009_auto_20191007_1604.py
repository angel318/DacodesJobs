# Generated by Django 2.2.5 on 2019-10-07 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empleados', '0008_auto_20191007_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='nombre',
            field=models.CharField(max_length=200, verbose_name='Nombre del empleado'),
        ),
    ]
