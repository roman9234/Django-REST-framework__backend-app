from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.models import ApiUser, Hotel, Room, Booking
from api.serializers import UserSerializer, HotelSerializer, RoomSerializer, BookingSerializer


# Create your views here.


# queryset - набор полей, которые будут отдаваться при запросах
class UserModelViewSet(viewsets.ModelViewSet):
    # можно настроить более сложную логику фильтрации и параметров
    queryset = ApiUser.objects.all()
    # по умолчанию ModelViewSet реализует все основные методы - GET POST итд
    # мы используем не все методы
    # http_method_names = ["post", "path", "get"]
    http_method_names = ["post", "get"]
    # Укажем сериализатор, который делали ранее.
    # Он будет использоваться для валидации данных фронтенда,
    # обновления и создания пользователя
    serializer_class = UserSerializer

    authentication_classes = []
    permissions_classes = []


# Добавляем остальные
# не перечисляем HTTP-методы, потому что это опционально
class HotelModelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    # Для доступа к команатм при запросе, можно использовать:
    # def retrieve(self, request, *args, **kwargs):

    # Но вместо этого мы сделаем отдельный endpoint
    # как называем метод, так и будет называться endpoint в нашем API

    # пишем декоратор action - означает что это именно метод rest_api
    # так как это rest_api, то метод принимаетпараметр request
    # раз он detail значит ещё принимает id primary key нашего отеля

    # http://127.0.0.1:8000/hotels/1/rooms
    @action(detail=True)
    def rooms(self, request, pk=None):
        # если отеля нет, вылезет ошибка 404
        hotel = get_object_or_404(Hotel.objects.all(), id=pk)
        # можно прописать через .rooms
        # так как мы указывали в related_name класса Room в models.py
        # фильтруем по условию bookings__isnull
        free_rooms = hotel.rooms.filter(bookings__isnull=True)
        return Response(
            # many=True так как мы возвращаем список комнат
            RoomSerializer(free_rooms, many=True).data
        )


class RoomModelViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BookingModelViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
