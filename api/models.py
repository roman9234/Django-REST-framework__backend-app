from django.contrib.auth.models import AbstractUser
from django.db import models


# так как User уже есть в библиотеке Django
# Встроенный User и его суперкласс AbstractUser уже имеют весь функционал ответственный за аутентификацию
# Так как в Django может быть только один объект для аутентификации, его нужно указать в settings.py
# AUTH_USER_MODEL = 'api.ApiUser'


class ApiUser(AbstractUser):
    ...




# Наследуем от модели
class Hotel(models.Model):
    # name это символьное поле с максимальной длиной 128
    name = models.CharField(max_length=128)


class Room(models.Model):
    # Есть встроенная валидация - не получится задать отрицательные значения
    num = models.PositiveIntegerField()
    # Ссылочный тип (внешний ключ)
    # related_name это имя, по которому мы будем получать у отеля его комнаты
    # models.CASCADE - каскадное удаление. Пишем без скобок ()
    hotel = models.ForeignKey(Hotel, related_name="rooms", on_delete=models.CASCADE)

class Booking(models.Model):
    room = models.ForeignKey(Room, related_name="bookings", on_delete=models.CASCADE)
    user = models.ForeignKey(ApiUser, related_name="user", on_delete=models.CASCADE)


# миграция - это специальный файл который есть в механизме Django ORM
# который описывает изменения в базе данных от какого-то момента времени














