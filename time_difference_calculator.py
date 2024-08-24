from datetime import datetime
from timezone_finder import get_city_timezone_google



def calculate_time_difference(city1, country1, city2, country2):
      
    
    timezone_obj1, _, _ = get_city_timezone_google(city1, country1)
    timezone_obj2, _, _ = get_city_timezone_google(city2, country2)
    
    if timezone_obj1 and timezone_obj2:
        # Extract the UTC offset in hours from the formatted_timezone strings
        offset1 = datetime.now(timezone_obj1).utcoffset().total_seconds() / 3600
        offset2 = datetime.now(timezone_obj2).utcoffset().total_seconds() / 3600
        
        # Calculate the difference in hours
        diff_hours = (offset2 - offset1)
        
        return diff_hours
    
    
    else:
        print("Unable to determine timezone for one or both cities.")
        return None
        

# Input of City
city1 = input("\nEnter name of first city to compare time difference : ")
country1 = input("Enter first city's Country/State/Province : ")
city2 = input("\nEnter name of second city to compare time difference : ")
country2 = input("Enter second city's Country/State/Province : ")

time_diff_hours = calculate_time_difference(city1, country1, city2, country2)

if time_diff_hours is not None:
    if time_diff_hours == 0:
        print(f"\nThere is no time difference between {city1}, {country1} and {city2}, {country2}.")
    else:
        print(f"\nThe time difference between {city1}, {country1} and {city2}, {country2} is {abs(time_diff_hours)} hours.")
        
        if time_diff_hours > 0:
            print(f"{city1}, {country1} is behind {city2}, {country2} by {abs(time_diff_hours)} hours.")
        else:
            print(f"{city1}, {country1} is ahead of {city2}, {country2} by {abs(time_diff_hours)} hours.")
else:
    print("\nUnable to calculate time difference.")