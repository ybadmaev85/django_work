# Generated by Django 4.2.3 on 2023-08-10 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('description', models.TextField(max_length=150, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, max_length=150, null=True, verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Изображение')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Цена за покупку')),
                ('creation', models.DateField(blank=True, null=True, verbose_name='Дата создания')),
                ('last_change', models.DateField(blank=True, null=True, verbose_name='Дата последнего изменения')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'собака',
                'verbose_name_plural': 'собаки',
                'ordering': ('name',),
            },
        ),
    ]