from django.conf.urls import url
from .views import CardListAPIView, CardDetailRetrieveAPIView


urlpatterns = [
    url('^card-list/$', CardListAPIView.as_view(), name='card-list'),
    url('^card/(?P<pk>\d+)/detail/$', CardDetailRetrieveAPIView.as_view(), name='card-history'),
]