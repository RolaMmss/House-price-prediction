from django.shortcuts import render
from django.conf import settings
import folium
import pandas as pd

# Create your views here.

def index(request):
    # context = {'a': 'HelloWorld!'}
    return render(request,'houseapp/index.html')#,context)

def predictPrice(request):
    context = {'a': 'Hello New  World!'}
    return render(request,'houseapp/index.html',context)

def get_center_latlong(df):
    # get the center of my map for plotting
    centerlat = (df['lat'].max() + df['lat'].min()) / 2
    centerlong = (df['long'].max() + df['long'].min()) / 2
    return centerlat, centerlong

def map_view(request):
    # Load data and create map
    df = pd.read_csv('data.csv')    
    center = get_center_latlong(df)
    map = folium.Map(location=center, zoom_start=10)
    
    # Add circles to map
    for i in range(len(df)):
        folium.Circle(
            location=[df.iloc[i]['lat'], df.iloc[i]['long']],
            radius=10,
            popup=folium.Popup(
                "<b>Price:</b> ${}<br><b>Zipcode:</b> {}".format(df.iloc[i]['price'], df.iloc[i]['zipcode']),
                max_width=200,
            ),
        ).add_to(map)

    # Render the map HTML code and pass it to the template
    map_html = map._repr_html_()
    context = {'map_html': map_html}
    return render(request, 'index.html', context)
