from ..models import Card, PurchaseHistoryInfo
from rest_framework import serializers


class CardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'seria_numb', 'card_number', 'release_date', 'activity_end_date', 'status',)


class PurchaseHistoryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseHistoryInfo
        fields = ('purchase_one_title', 'purchase_amount', 'purchase_date',)


class CardDetailSerializer(serializers.ModelSerializer):
    purchase_history = serializers.SerializerMethodField()

    class Meta:
        model = Card
        fields = ('id', 'purchase_history',)

    def get_purchase_history(self, obj):
        return PurchaseHistoryInfoSerializer(obj.purchasehistoryinfo_set.all(), many=True, context={"request": self.context.get("request")}).data


class CardDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'seria_numb',)
