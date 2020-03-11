from django.contrib import admin
from .models import Card, PurchaseHistoryInfo
from django.contrib.auth.models import Group
# Register your models here.


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass


@admin.register(PurchaseHistoryInfo)
class PurchaseHistoryInfoAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(Group)
