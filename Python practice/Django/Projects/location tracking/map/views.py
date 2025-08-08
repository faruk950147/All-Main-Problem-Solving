from django.shortcuts import render
from django.views import View
from django.contrib import messages
from phonenumbers import parse, is_valid_number, timezone, geocoder, carrier
from phonenumbers.phonenumberutil import NumberParseException
from opencage.geocoder import OpenCageGeocode
from decouple import config
import folium
from map.forms import NumberForm

class MapView(View):
    def get(self, request):
        return render(request, 'map/map.html', {'form': NumberForm()})
    
    def post(self, request):
        form = NumberForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            api_key = config("OPENCAGE_API_KEY")  
            try:
                phone_number = parse(number)
                if not is_valid_number(phone_number):
                    messages.error(request, "Invalid phone number.")
                    return render(request, 'map/map.html', {'form': form})
                
                location = geocoder.description_for_number(phone_number, "en")
                time_zone = timezone.time_zones_for_number(phone_number)
                carrier_name = carrier.name_for_number(phone_number, "en")
                
                result = OpenCageGeocode(api_key).geocode(location)
                lat, lng = result[0]['geometry'].values()
                
                map_object = folium.Map(location=[lat, lng], zoom_start=15)
                folium.Marker([lat, lng], popup=location).add_to(map_object)
                map_html = map_object._repr_html_()

                messages.success(request, 'Location found successfully!')
                return render(request, 'map/map.html', {
                    'form': form,
                    'map': map_html,
                    'location': location,
                    'time_zone': time_zone,
                    'carrier_name': carrier_name,
                })
            except NumberParseException:
                messages.error(request, "Invalid phone number format.")
            except Exception as e:
                messages.error(request, f"Error: {e}")
        
        return render(request, 'map/map.html', {'form': form})
