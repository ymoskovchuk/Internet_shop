# Generated by Django 2.2 on 2021-03-26 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20210326_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Customer', verbose_name='Владелец'),
        ),
    ]
