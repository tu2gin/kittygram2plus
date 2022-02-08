from rest_framework import viewsets

from .models import Achievement, Cat, User

from .serializers import AchievementSerializer, CatSerializer, UserSerializer
from .pagination import CatsPagination
from .permissions import ReadOnly, OwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.throttling import AnonRateThrottle
from rest_framework import filters

from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination



class CatViewSet(viewsets.ModelViewSet):
# Фильтрация

    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = (OwnerOrReadOnly,)
    # Указываем фильтрующий бэкенд DjangoFilterBackend
    # Из библиотеки django-filter
    filter_backends = (DjangoFilterBackend,)
    # Временно отключим пагинацию на уровне вьюсета, 
    # так будет удобнее настраивать фильтрацию
    pagination_class = None
    # Фильтровать будем по полям color и birth_year модели Cat
    filterset_fields = ('color', 'birth_year')
    search_fields = ('name',)

# + Поиск

    # queryset = Cat.objects.all()
    # serializer_class = CatSerializer
    # permission_classes = (OwnerOrReadOnly,)
    # # Добавим в кортеж ещё один бэкенд
    # filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # pagination_class = None
    # filterset_fields = ('color', 'birth_year')
    # search_fields = ('name',) 

# + Сортрировка

    # queryset = Cat.objects.all()
    # serializer_class = CatSerializer
    # permission_classes = (OwnerOrReadOnly,)
    # filter_backends = (DjangoFilterBackend, filters.SearchFilter,
    #                    filters.OrderingFilter)
    # pagination_class = None
    # filterset_fields = ('color', 'birth_year')
    # search_fields = ('name',)
    # ordering_fields = ('name', 'birth_year') 


# + Упорядочим выдачу наших котиков по умолчанию по году рождения

    # queryset = Cat.objects.all()
    # serializer_class = CatSerializer
    # permission_classes = (OwnerOrReadOnly,)
    # filter_backends = (DjangoFilterBackend, filters.SearchFilter,
    #                    filters.OrderingFilter)
    # pagination_class = None
    # filterset_fields = ('color', 'birth_year')
    # search_fields = ('name',)
    # ordering_fields = ('name', 'birth_year')
    # ordering = ('birth_year',)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user) 
    
    def get_permissions(self):
        # Если в GET-запросе требуется получить информацию об объекте
        if self.action == 'retrieve':
            # Вернем обновленный перечень используемых пермишенов
            return (ReadOnly(),)
        # Для остальных ситуаций оставим текущий перечень пермишенов без изменений
        return super().get_permissions() 


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer