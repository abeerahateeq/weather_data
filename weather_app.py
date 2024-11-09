import requests
import pandas as pd
import streamlit as st

API_KEY = '9MMJ89HLQV83XVKLS7DR4JXSF'  

cities = ['Lahore', 'Islamabad', 'Karachi', 'Faisalabad']

def get_weather_data(city):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key={API_KEY}&contentType=json"
    response = requests.get(url)
    return response.json()

def fetch_weather_data():
    data = []
    for city in cities:
        weather = get_weather_data(city)
        for day in weather['days']:
            data.append({
                'City': city,
                'Date': day['datetime'],
                'Temperature': day['temp'],
                'Condition': day['conditions']
            })
    return pd.DataFrame(data)

# Streamlit display
def main():
    st.title("Weather Forecast for Multiple Cities")
    
    # Fetch weather data
    weather_data = fetch_weather_data()
    
    # Search bar to filter cities
    search_city = st.text_input("Search for a city")
    if search_city:
        weather_data = weather_data[weather_data["City"].str.contains(search_city, case=False)]
    
    # Sort by temperature or city
    sort_option = st.selectbox("Sort by", ["City", "Temperature"])
    if sort_option == "Temperature":
        weather_data = weather_data.sort_values(by="Temperature")
    else:
        weather_data = weather_data.sort_values(by="City")
    
    # Display weather data in a table
    st.table(weather_data)

if __name__ == "__main__":
    main()
