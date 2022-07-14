from django import forms

class ListingForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(label='Description', max_length=400)
    start_bid = forms.CharField(label='Start Bid', max_length=400)
    image = forms.CharField(label='Image URL', max_length=400)