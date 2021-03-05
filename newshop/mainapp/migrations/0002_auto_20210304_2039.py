# Generated by Django 2.2 on 2021-03-04 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='final_price',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Финальная цена'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Customer', verbose_name='Владелец'),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_products', to='mainapp.Cart', verbose_name='Корзина'),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='final_price',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Финальная цена'),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Customer', verbose_name='Покупатель'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=255, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Картинка')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('diagonal', models.CharField(max_length=255, verbose_name='Диагональ')),
                ('display_type', models.CharField(max_length=255, verbose_name='Тип дисплея')),
                ('resolution', models.CharField(max_length=255, verbose_name='Разрешение экрана')),
                ('accumulator', models.CharField(max_length=255, verbose_name='Объем батареи')),
                ('ram', models.CharField(max_length=255, verbose_name='Оперативная память')),
                ('sd', models.BooleanField(default=True, verbose_name='Наличие карты памяти')),
                ('sd_volume', models.CharField(max_length=255, verbose_name='Объем карты памяти')),
                ('main_cam_mp', models.CharField(max_length=255, verbose_name='Разрешение основной камеры')),
                ('front_cam_mp', models.CharField(max_length=255, verbose_name='Разрешение фронтальной камеры')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Картинка')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('diagonal', models.CharField(max_length=255, verbose_name='Диагональ')),
                ('display_type', models.CharField(max_length=255, verbose_name='Тип дисплея')),
                ('processor_freq', models.CharField(max_length=255, verbose_name='Частота процессора')),
                ('ram', models.CharField(max_length=255, verbose_name='Оперативная память')),
                ('gpu', models.CharField(max_length=255, verbose_name='Видеокарта')),
                ('time_without_charge', models.CharField(max_length=255, verbose_name='Время без зарядки')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
