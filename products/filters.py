import django_filters
from .models import Orders

class OrderHistoryFilter(django_filters.FilterSet):

    class Meta:
        model = Orders
        fields = ('accountid',)
