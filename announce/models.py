from django.db import models

class Announce(models.Model):
    class Meta:
        verbose_name = 'Объявление',
        verbose_name_plural = 'Объявления'
    name =models.CharField('Название обьявления',max_length=256)
    price = models.PositiveIntegerField('Цена')
    production_year = models.DateField("Год выпуска")
    mileage = models.PositiveIntegerField('Пробег')
    body_type = models.CharField('Тип кузова',max_length=64)
    capacity = models.FloatField('Объем')
    power = models.PositiveSmallIntegerField('Мощность')
    gear = models.CharField('Привод',max_length=32)
    transmission = models.CharField('КПП',max_length=32)
    steering_wheel = models.CharField('Руль',max_length=32)
    description = models.TextField('Описание')
    city = models.CharField('Город',max_length=64)

    def __str__(self):
        return self.name

