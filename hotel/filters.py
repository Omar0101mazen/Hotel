import django_filters
from .models import Hotel
class HotelFilter(django_filters.FilterSet):
    der_Hotelname = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Hotel
        fields = ['Entfernung','preis','Lage','Passt','Strand','Essen']
        # exclude =  ('slug','owner','img','published_at','salary','Vacancy')
        