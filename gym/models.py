from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, time, timedelta

# Create your models here.

class Trainer(models.Model):
    #user = models.OneToOneField(User, on_delete= models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=100, verbose_name='Имя', blank=True, null=True)
    surname = models.CharField(max_length=100, verbose_name='Фамилия', blank=True, null=True)
    about = models.TextField(blank=True, verbose_name='Про себе')
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d/", verbose_name='Фото')
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Ціна за заняття')
    
    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'

    def __str__(self) -> str:
        return f'Тренер "{self.name}"'



class Abonement(models.Model):
    name = models.CharField(max_length=100, verbose_name='Назва')
    about = models.TextField(verbose_name='Описание абонемента')
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Ціна')
    
    class Meta:
        verbose_name = 'Абонемент'
        verbose_name_plural = 'Абонементы'
    
    def __str__(self) -> str:
        return f'Абонемент "{self.name}"'






