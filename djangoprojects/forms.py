from django import forms
 
# creating a form

class GeeksForm(forms.Form):

    title = forms.CharField()

    description = forms.CharField() 