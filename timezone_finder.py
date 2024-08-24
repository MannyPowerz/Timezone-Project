from datetime import datetime
from collections import namedtuple
import pytz
import googlemaps
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('GOOGLEMAPS_API_KEY')

gmaps_key = googlemaps.Client(key=api_key)

def get_city_timezone_google(city_name, country_name=None):
    query = f"{city_name}, {country_name}" if country_name else city_name
    geocode_result = gmaps_key.geocode(query)
    
    if geocode_result:
        # Extracting lattiutude and longittude from first item generated in library using keys in dictionary using inputed query (city and country) 
        lat, lon = geocode_result[0]['geometry']['location']['lat'], geocode_result[0]['geometry']['location']['lng']
        
        # Requesting Timezone Information from Dictionary from obtained lat and lon 
        timezone_info = gmaps_key.timezone((lat, lon))
        
        # Extract the timezone identifier from the dictionary
        timezone_str = timezone_info['timeZoneId']
        
        
        #Converting Timezone String to Pytz Object obtained from the API
        timezone_obj = pytz.timezone(timezone_str)

        
        # Get the current time in the timezone and format it to include the UTC offset for daytime saving reason such as EST/EDT
        current_time = datetime.now(timezone_obj)

        #formatted_time = current_time.strftime("%Y-%m-%d %H:%M %Z%z")
        formatted_timezone = current_time.strftime("%Z%z")
        
        timezone_name = timezone_info['timeZoneName']
        
        return   timezone_obj, timezone_name, formatted_timezone
    
    else:
        print(f"No location found for {query}. Please check the city and/or country name.")
        return None, None, None


  
# Input for Code 
if __name__ == "__main__":
    city_name = input("Enter name of city: ")
    country_name = input("Enter name of country, province, or state: ")
    timezone_obj, timezone_name, formatted_timezone = get_city_timezone_google(city_name, country_name)



    if timezone_obj:
        print(f"\nThe timezone for {city_name}, {country_name} is {timezone_name} {formatted_timezone}\n")
    
    else:
        print("Unable to determine timezone.\n")

    
    
 