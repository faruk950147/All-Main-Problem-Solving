import phonenumbers
from phonenumbers import timezone, geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium
import webbrowser

def Location(numbers):
    api_key = "992f1a79901b4948892a93c128f9f515"    
    phone_number = phonenumbers.parse(numbers)
    valid = phonenumbers.is_valid_number(phone_number)
    if valid:
        location = geocoder.description_for_number(phone_number, "en")
        if location:
            print(f"Location: {location}")
        else:
            print("Location info not found.")

        time_zone = timezone.time_zones_for_number(phone_number)
        if time_zone:
            print(f"Time Zone: {time_zone}")
        else:
            print("Time zone info not found.")

        service_provider = carrier.name_for_number(phone_number, "en")
        if service_provider:
            print(f"Service Provider: {service_provider}")
        else:
            print("Service provider info not found.")

        # OpenCage Geocode to get latitude and longitude
        # OpenCageGeocode(api_key) is a constructor function in class OpenCageGeocode
        # geocode(location) is a method in class OpenCageGeocode and return a list of dictionaries 
        results = OpenCageGeocode(api_key).geocode(location) 

        if results and len(results):
            latitude = results[0]['geometry']['lat']
            longitude = results[0]['geometry']['lng']
            print(f"Latitude: {latitude}, Longitude: {longitude}")

            # Create a map
            map = folium.Map(location=[latitude, longitude], zoom_start=9)
            folium.Marker([latitude, longitude], popup=location).add_to(map)

            # Save the map as an HTML file
            map.save("phone_location.html")
            print("Map saved as phone_location.html")   
            webbrowser.open("phone_location.html")
        else:
            print("Location info not found.")
    else:
        print("Invalid Number")

Location("+8801581759301")
