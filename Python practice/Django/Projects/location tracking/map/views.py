from django.shortcuts import render
from django.views import generic

# Create your views here.

class MapView(generic.View):
    def get(self, request):
        return render(request, 'map/map.html')

