# Generated by Django 3.1.4 on 2020-12-11 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название обьявления')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('production_year', models.DateField(verbose_name='Год выпуска')),
                ('mileage', models.PositiveIntegerField(verbose_name='Пробег')),
                ('body_type', models.CharField(max_length=64, verbose_name='Тип кузова')),
                ('capacity', models.FloatField(verbose_name='Объем')),
                ('power', models.PositiveSmallIntegerField(verbose_name='Мощность')),
                ('gear', models.CharField(max_length=32, verbose_name='Привод')),
                ('transmission', models.CharField(max_length=32, verbose_name='КПП')),
                ('steering_wheel', models.CharField(max_length=32, verbose_name='Руль')),
                ('description', models.TextField(verbose_name='Описание')),
                ('city', models.CharField(max_length=64, verbose_name='Город')),
            ],
        ),
    ]
