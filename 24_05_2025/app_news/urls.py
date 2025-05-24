from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    NewsPageNumberPaginationViewSet,
    NewsLimitOffsetPaginationViewSet,
    NewsCustomPaginationViewSet


)

roter=DefaultRouter()
roter_2=DefaultRouter()
roter_3=DefaultRouter()

roter.register('news-number-page',NewsPageNumberPaginationViewSet,basename='news-nurmal-page')
roter_2.register('news-limitoffset-page',NewsLimitOffsetPaginationViewSet,basename='limit-offset-page')
roter_3.register('news-custom-page',NewsCustomPaginationViewSet,basename='news-custom-page')

urlpatterns = [

]

urlpatterns+=roter.urls
urlpatterns+=roter_2.urls
urlpatterns+=roter_3.urls