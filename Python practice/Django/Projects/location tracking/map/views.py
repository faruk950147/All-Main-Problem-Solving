from django.shortcuts import render
from django.views import View
from django.contrib import messages
import phonenumbers
from phonenumbers import timezone, geocoder as phone_geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium
from map.forms import NumberForm

class MapView(View):
    def get(self, request):
        form = NumberForm()
        return render(request, 'map/map.html', {'form': form})
    
    def post(self, request):
        form = NumberForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            api_key = "992f1a79901b4948892a93c128f9f515"    

            phone_number = phonenumbers.parse(number)
            time_zone = timezone.time_zones_for_number(phone_number)
            carrier_name = carrier.name_for_number(phone_number, 'en')
            region = phone_geocoder.description_for_number(phone_number, 'en')

            oc_geocoder = OpenCageGeocode(api_key)
            result = oc_geocoder.geocode(region)
            lat = result[0]['geometry']['lat']
            lng = result[0]['geometry']['lng']

            # Folium Map as HTML
            map_object = folium.Map(location=[lat, lng], zoom_start=15)
            map_html = map_object._repr_html_()

            messages.success(request, 'Location found successfully!')
            return render(request, 'map/map.html', {
                'form': form,
                'map': map_html,
                'time_zone': time_zone,
                'carrier_name': carrier_name,
                'region': region
            })
        return render(request, 'map/map.html', {'form': form})

            

