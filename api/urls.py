# В этом файле будет шаблон нашего приложения
from rest_framework.routers import DefaultRouter

from api.views import UserModelViewSet, HotelModelViewSet, RoomModelViewSet, BookingModelViewSet

# используем роутер из rest_framework
router = DefaultRouter()
# в этом роутере мы регистрируем URL связанный с нашими пользователями
# В нём указываем созданный ранее ViewSet
router.register('users', UserModelViewSet)
router.register('hotels', HotelModelViewSet)
router.register('rooms', RoomModelViewSet)
router.register('bookings', BookingModelViewSet)

urlpatterns = [

]
# Расширяем urlpatterns из роутера, из переменной urls
urlpatterns.extend(router.urls)
# urlpatterns нужен на случай если мы захотим добавить какие-то переменные не связанные с rest_framework
# то тогда можно будет добавить в urlpatterns обычный path как в Django без модуля rest_framework



# После изменений в этом файле, нужно изменить urls проекта
# path('', include('api.urls')),





