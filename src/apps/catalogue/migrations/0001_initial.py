# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 08:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OptionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Option group',
                'ordering': ['name'],
                'verbose_name_plural': 'Option groups',
            },
        ),
        migrations.CreateModel(
            name='OptionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Параметр')),
                ('option_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='groups', related_query_name='group', to='catalogue.OptionGroup')),
            ],
            options={
                'verbose_name': 'Option',
                'ordering': ['name'],
                'verbose_name_plural': 'Options',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Category',
                'ordering': ['name'],
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='Цена')),
                ('product_image', models.ImageField(upload_to='product')),
                ('rating', models.FloatField(default=0, verbose_name='Рейтинг')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создан')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлен')),
                ('status', models.CharField(choices=[('d', 'Добавлен'), ('p', 'Опубликован'), ('w', 'Изъят')], default='d', max_length=1, verbose_name='Текущий статус')),
                ('product_options', models.ManyToManyField(to='catalogue.OptionGroup', verbose_name='Доступные опции')),
            ],
            options={
                'verbose_name': 'Товар',
                'ordering': ['name'],
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='ProductRecommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSpecial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('options', models.ManyToManyField(blank=True, default='', to='catalogue.OptionGroup', verbose_name='Options')),
            ],
            options={
                'verbose_name': 'Product type',
                'ordering': ['name'],
                'verbose_name_plural': 'Product types',
            },
        ),
        migrations.AddField(
            model_name='productitem',
            name='product_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='types', related_query_name='type', to='catalogue.ProductType', verbose_name='Тип'),
        ),
    ]
