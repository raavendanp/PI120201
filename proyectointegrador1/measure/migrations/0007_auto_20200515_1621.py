# Generated by Django 3.0.3 on 2020-05-15 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measure', '0006_measure_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measure',
            name='Producto',
            field=models.CharField(max_length=20, verbose_name='Producto'),
        ),
    ]