# House-price-prediction in King County, WA, USA
Develop an application to predict the price of a house (pandas-machine learning-Django)
Exploratory data analysis can be found in data_cleaning_analysis.ipynb
Preparation of data can be found in data_preparation.ipynb
Models and price prediction  can be found in data_modelisation.ipynb

# Pacakge required
folium for the geo heat map. Installation pip install folium.

Other common packages: pandas, numpy, seaborn, statsmodels.api, sklearn, matplotlib

# Dataset Description
This dataset contains house sale prices for King County, which includes Seattle. It includes homes sold between May 2014 and May 2015. It's a great dataset for evaluating regression models.

The dataset is retrieved from Kaggle. It is published on 08/25/2016. The source is believed to be reliable because all housing information is public data. It is a famous dataset, and the features are complete.

Along with house price (target) it consists of an ID, date, and 18 house features.

    Id: Unique ID for each home sold
    Date: Date of the home sale
    Price: Price of each home sold (target)
    Bedrooms: Number of bedrooms
    Bathrooms: Number of bathrooms, where .5 accounts for a room with a toilet but no shower
    Sqft_living: Square footage of the apartments interior living space
    Sqft_lot: Square footage of the land space
    Floors: Number of floors
    Waterfront: A dummy variable for whether the apartment was overlooking the waterfront or not 10.View: An index from 0 to 4 of how good the view of the property was 11.Condition: An index from 1 to 5 on the condition of the apartment,
    Grade: An index from 1 to 13, where 1-3 falls short of building construction and design, 7 has an average level of construction and design, and 11-13 have a high quality level of construction and design
    Sqft_above: The square footage of the interior housing space that is above ground level
    Sqft_basement: The square footage of the interior housing space that is below ground level
    Yr_built: The year the house was initially built
    Yr_renovated: The year of the house’s last renovation
    Zipcode: What zipcode area the house is in
    Lat: Lattitude
    Long: Longitude
    Sqft_living15: The square footage of interior housing living space for the nearest 15 neighbors
    Sqft_lot15: The square footage of the land lots of the nearest 15 neighbors

# Conclusions

    The price (target) has many outliers, and it is positively skewed, which makes it hard to generate a proper model to predict the price.

    From EDA, we understand several key findings:
        (1) The living square footage is highly correlated with the price.
        (2) The grade is highly correlated with the price
        (3) The number of bathrooms positively correlated with the price.
        (4) The view also determines the price.
        (5) Since most people don't have a basement, so square footage above the ground is correlated with the living square footage.
        (6) Usually, the neighborhood has a similar size of the living space.
        (7) The age of the house doesn't have a clear trend contributing to the price.
        (8) The house with the renovation can sell slightly higher than the houses they don't.

# Models used:
  - KNeighborsRegressor 
  - LinearRegression
