from django.shortcuts import render
from .models import Hotel
from .filters import HotelFilter
from django.core.paginator import Paginator
# Create your views here.
def hotel_list(request):
    hotel = Hotel.objects.all()
    myfilter = HotelFilter(request.GET,queryset=hotel)
    hotel = myfilter.qs
    paginator = Paginator(hotel, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    
    return render(request,'hotel_list.html',{'hotel':page_obj,'myfilter':myfilter,'page_obj':page_obj})