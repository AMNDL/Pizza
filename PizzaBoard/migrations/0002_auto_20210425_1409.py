# Generated by Django 3.2 on 2021-04-25 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PizzaBoard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='weight',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Вес'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_time',
            field=models.DateTimeField(verbose_name='Время доставки'),
        ),
    ]
