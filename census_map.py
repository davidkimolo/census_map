# Importing required libraries
import folium
import pandas

# Getting the longitude and latitude of all the countries
countries_locations = pandas.read_csv("countries.csv")
population = pandas.read_csv("pop_total_ds2_en_v2.csv")
lat = list(countries_locations["latitude"])
lon = list(countries_locations["longitude"])
pupltn = list(population["column_b"])

# trying to convert to numeric so that i do not have any 'NaNs'
lt = pandas.to_numeric(lat)
lg = pandas.to_numeric(lon)
ppl = pandas.to_numeric(pupltn, errors='coerce')


# change popup color depending on population
def icon_color (country_population):
    if country_population < 100:
        return "blue"
    elif country_population < 1000:
        return "purple"
    elif country_population < 10000:
        return "orange"
    elif country_population < 100000:
        return "darkgreen"
    elif country_population < 1000000:
        return "beige"
    elif country_population < 10000000:
        return  "black"
    elif country_population < 100000000:
        return "darkblue"
    else:
        return "red"


# Looping through the countries 
geo_map = folium.Map(location=[8.7832, 34.5085], zoom_start=3.8)
background = folium.FeatureGroup(name= "Population map")
for lt, lg, ppl in zip(lat, lon, pupltn):
    background.add_child(folium.Marker(location= [lt , lg], popup= f"population: {ppl}", icon=folium.Icon(color=icon_color(ppl))))

# Rendering, displaying to the web
geo_map.add_child(background)
geo_map.save("map.html")

