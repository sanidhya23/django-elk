from django import forms

class CityAddForm(forms.Form):
    city_name = forms.CharField(label='City')
    city_population = forms.IntegerField(label='Polulation', min_value=1)