from django.shortcuts import render
from .models import Detail

def details_view(request):
    details_data = Detail.objects.all()
    return render(request, 'appinfo/details.html', {'details_data': details_data})
    # return render(request, 'appinfo/details.html', {'details_data': details_data, 'location_data': location_data, 'images': images})
