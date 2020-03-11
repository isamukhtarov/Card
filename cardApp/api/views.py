from .serializers import CardListSerializer, CardDetailSerializer, CardDeleteSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics


class CardListAPIView(generics.ListAPIView):
    serializer_class = CardListSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    # 10 and 11 lines execute поиск по этим же полям given in task
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['seria_numb', 'card_number', 'release_date', 'activity_end_date', 'status']
    paginate_by = 50


#This class retrieve card history and allow delete this card
class CardDetailRetrieveAPIView(generics.RetrieveDestroyAPIView):
    # lookup_field = 'id'
    serializer_class = CardDetailSerializer
    queryset = serializer_class.Meta.model.objects.all()
