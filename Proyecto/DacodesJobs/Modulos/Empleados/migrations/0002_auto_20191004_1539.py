# Generated by Django 2.2.5 on 2019-10-04 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empleados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='puesto',
            field=models.CharField(choices=[('Frontend', 'Frontend'), ('Backend', 'Backend')], default='n/a', max_length=6, verbose_name='Puesto'),
        ),
    ]