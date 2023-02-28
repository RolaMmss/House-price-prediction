from django import forms

class PriceForm(forms.ModelForm):
    bedrooms = forms.IntegerField(required=True)
    bathrooms = forms.IntegerField(required=True)
    sqft_living = forms.IntegerField(required=True)
    sqft_lot = forms.IntegerField(required=True)
    floors = forms.IntegerField(required=True)
    waterfront = forms.IntegerField(required=True)
    view = forms.IntegerField(required=True)
    condition = forms.IntegerField(required=True)
    grade = forms.IntegerField(required=True)
    sqft_above = forms.IntegerField(required=True)
    sqft_basement = forms.IntegerField(required=True)
    zipcode = forms.IntegerField(required=True)




