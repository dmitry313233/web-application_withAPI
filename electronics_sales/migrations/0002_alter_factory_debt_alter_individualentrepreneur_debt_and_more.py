# Generated by Django 5.0 on 2023-12-19 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics_sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factory',
            name='debt',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Задолженность'),
        ),
        migrations.AlterField(
            model_name='individualentrepreneur',
            name='debt',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Задолженность'),
        ),
        migrations.AlterField(
            model_name='retailnetwork',
            name='debt',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Задолженность'),
        ),
    ]
