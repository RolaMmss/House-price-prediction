from django.shortcuts import render, redirect
from django.conf import settings
import folium
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import GridSearchCV
from . import forms
from .forms import PriceForm
import pickle


# # Create your views here.
# df = pd.read_csv('data.csv')             # without columns 'id' , 'date'   + 'year' 
# df_4 = pd.read_csv('data4.csv') 

with open('trained_pipe.pkl','rb') as f:
    knn=pickle.load(f)

def index(request):
    context ={}
    context['form']= PriceForm()
    return render(request,'houseapp/index.html',context)

# def predictPrice(request):
#     # Check if the form has been submitted
#     if request.method == 'POST':
#         # Get the form data
#         form = PriceForm(request.POST)
#         # Check if the form data is valid
#         if form.is_valid():
#             # Get the input data
#             input_data = [form.cleaned_data['zipcode'],
#                           form.cleaned_data['bedrooms'],
#                           form.cleaned_data['bathrooms'],
#                           form.cleaned_data['sqft_living'],
#                           form.cleaned_data['sqft_lot'],
#                           form.cleaned_data['floors'],
#                           form.cleaned_data['waterfront'],
#                           form.cleaned_data['view'],
#                           form.cleaned_data['condition'],
#                           form.cleaned_data['grade'],
#                           form.cleaned_data['sqft_above'],
#                           form.cleaned_data['sqft_basement'],]
#             # Make a prediction using the ML model
#             prediction = knn.predict([input_data])[0]
#             # Render the prediction to the template
#             return render('prediction', {'prediction':prediction})    
#         else:
#             form = PriceForm()
        
#     return render(request,'houseapp/index.html', {'form': form})


def predictPrice(request):
    # Check if the form has been submitted
    if request.method == 'POST':
        # Get the form data
        form = PriceForm(request.POST)
        # Check if the form data is valid
        if form.is_valid():
            # Get the input data
            
            # Make a prediction using the ML model
            #prediction = knn.predict([input_data])[0]
            # Render the prediction to the template
            form.save()
            return redirect('prediction')    
        else:
            form = PriceForm()
        
    return render(request,'houseapp/index.html', {'form': form})


def prediction(request):
    bedrooms = int(request.POST['bedrooms'])     
    bathrooms =float( request.POST['bathrooms'])     
    sqft_living = int(request.POST['sqft_living'])     
    sqft_lot = int(request.POST['sqft_lot'])     
    floors = float(request.POST['floors'])     
    waterfront = int(request.POST['waterfront'])  
    view = int(request.POST['view'])     
    condition = int(request.POST['condition'])     
    grade = int(request.POST['grade'])     
    sqft_above = int(request.POST['sqft_above'])   
    sqft_basement = int(request.POST['sqft_basement']) 
    zipcode = int(request.POST['zipcode'])   
    done_reno = int(request.POST['done_reno'])  
    age_house = int(request.POST['age_house'])    

 
    
    data = {'bedrooms': [bedrooms],         
           'bathrooms': [bathrooms],         
           'sqft_living': [sqft_living],         
           'sqft_lot': [sqft_lot],         
           'floors': [floors],         
           'waterfront': [waterfront],
           'view': [view],         
           'condition': [condition],
           'grade': [grade],         
           'sqft_above': [sqft_above],
           'sqft_basement': [sqft_basement],
           'zipcode': [zipcode],
           'done_reno': [done_reno],
           'age_house': [age_house]}
    df=pd.DataFrame(data, index=[0])
    prediction = knn.predict(df)[0]
     # Create a new form object to be displayed on the page
    form = PriceForm()
    # Pass the form and the prediction in the context
    context = {'form': form, 'prediction': prediction}
    return render(request,'houseapp/index.html', context)


# def get_center_latlong(df):
#     # get the center of my map for plotting
#     centerlat = (df['lat'].max() + df['lat'].min()) / 2
#     centerlong = (df['long'].max() + df['long'].min()) / 2
#     return centerlat, centerlong

# def map_view(request):
#     # Load data and create map
#     df = pd.read_csv('data.csv')    
#     center = get_center_latlong(df)
#     map = folium.Map(location=center, zoom_start=10)
    
#     # Add circles to map
#     for i in range(len(df)):
#         folium.Circle(
#             location=[df.iloc[i]['lat'], df.iloc[i]['long']],
#             radius=10,
#             popup=folium.Popup(map_view
#                 "<b>Price:</b> ${}<br><b>zipcode:</b> {}".format(df.iloc[i]['price'], df.iloc[i]['zipcode']),
#                 max_width=200,
#             ),
#         ).add_to(map)

#     # Render the map HTML code and pass it to the template
#     map_html = map._repr_html_()
#     context = {'map_html': map_html}
#     return render(request, 'index.html', context)
