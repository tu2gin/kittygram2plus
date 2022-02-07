from rest_framework import viewsets

from .models import Achievement, Cat, User

from .serializers import AchievementSerializer, CatSerializer, UserSerializer
from .permissions import ReadOnly

from rest_framework import permissions
from rest_framework.throttling import AnonRateThrottle


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_classes = (AnonRateThrottle,)  # Подключили класс AnonRateThrottle 
    # Для любых пользователей установим кастомный лимит 1 запрос в минуту
    throttle_scope = 'low_request' 

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