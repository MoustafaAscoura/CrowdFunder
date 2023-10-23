from datetime import datetime
from typing import Any
from django import forms
from .models import Project



class ProjectForm(forms.ModelForm):
    categories = (('Social','Social'),('Humanitarian', 'Humanitarian'),
                  ('Health', 'Health'),('Education','Education'),
                  ('Political','Political')) 
    category = forms.ChoiceField(choices=categories)
    start_time = forms.DateTimeField(widget=forms.NumberInput(attrs={'type':'date'}),required=False)
    end_time = forms.DateTimeField(widget=forms.NumberInput(attrs={'type':'date'}),required=False)
    tags = forms.CharField(widget=forms.TextInput(
          attrs={'data-role':"taginput",'data-max-tags':"6",'data-random-color':"true"})
          ,required=False)

    class Meta:
        model = Project
        exclude = ['user']

    def clean_tags(self):
        return self.cleaned_data.get('tags').split(',')

    def clean(self):
        start_date = self.cleaned_data.get('start_time')
        end_date = self.cleaned_data.get('end_time')
        if datetime.now().date() > start_date.date():
            msg = "Start date shouldn't be less than today."
            self._errors["start_time"] = self.error_class([msg])
        
        if end_date <= start_date:
            msg = "End date should be greater than start date."
            self._errors["end_time"] = self.error_class([msg])

