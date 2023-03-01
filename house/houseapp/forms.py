from django import forms

class PriceForm(forms.Form):
    VIEW_WATERFRONT_CHOICES = [
    (1, 'with'),
    (0, 'without'),]
    
    bedrooms = forms.IntegerField(required=True, min_value=0, max_value= 33)
    bathrooms = forms.FloatField(required=True, min_value=0,max_value=8,step_size=0.25)
    sqft_living = forms.IntegerField(required=True, min_value=0)
    sqft_lot = forms.IntegerField(required=True, min_value=0)
    floors = forms.FloatField(required=True, min_value=0,max_value=3.5,step_size=0.5)
    waterfront = forms.ChoiceField(choices=VIEW_WATERFRONT_CHOICES, required=True) 
    view = forms.ChoiceField(choices=VIEW_WATERFRONT_CHOICES, required=True)    
    condition = forms.IntegerField(required=True, min_value=0,max_value=5)
    grade = forms.IntegerField(required=True, min_value=0,max_value=13)
    sqft_above = forms.IntegerField(required=True, min_value=0)
    sqft_basement = forms.IntegerField(required=True, min_value=0)
    zipcode = forms.IntegerField(required=True, min_value=0)
    done_reno = forms.ChoiceField(choices=VIEW_WATERFRONT_CHOICES, required=True)    
    age_house = forms.IntegerField(required=True, min_value=0, max_value= 115)

    

