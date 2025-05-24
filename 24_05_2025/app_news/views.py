
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response
from .models import News
from .serializers import NewsSerializer,NewsListSerializer
from .pagination import CustomPagination
from .throttles import ListOnlyThrottle

class NewsPageNumberPaginationViewSet(ModelViewSet):
    queryset =News.objects.all()
    pagination_class=PageNumberPagination
    serializer_class=NewsSerializer

    def get_serializer_class(self):
        if self.action=='list':
            return NewsListSerializer
        return NewsSerializer

    def get_throttles(self):
        if self.action=='list':
            return [ListOnlyThrottle()]
        return []
        

class NewsLimitOffsetPaginationViewSet(ModelViewSet):
    queryset =News.objects.all()
    pagination_class=LimitOffsetPagination
    serializer_class=NewsSerializer

    def get_serializer_class(self):
        if self.action=='list':
            return NewsListSerializer
        return NewsSerializer


class NewsCustomPaginationViewSet(ModelViewSet):
    queryset =News.objects.all()
    pagination_class=CustomPagination
    serializer_class=NewsSerializer

    def get_serializer_class(self):
        if self.action=='list':
            return NewsListSerializer
        return NewsSerializer
