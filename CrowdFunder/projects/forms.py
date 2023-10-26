from datetime import datetime
from typing import Any
from django import forms
from .models import Project, Photo
from django.forms import ClearableFileInput, FileField 
from django.core.validators import validate_image_file_extension
from django.core.exceptions import ValidationError

class MultipleFileInput(ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(FileField):
    default_validators = [validate_image_file_extension]
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class ProjectForm(forms.ModelForm):
    categories = (('Social','Social'),('Humanitarian', 'Humanitarian'),
                  ('Health', 'Health'),('Education','Education'),
                  ('Political','Political')) 

    category = forms.ChoiceField(choices=categories)
    start_time = forms.DateTimeField(initial=datetime.now().date(),widget=forms.NumberInput(attrs={'type':'date'}),required=False)
    end_time = forms.DateTimeField(initial=datetime.now().date(),widget=forms.NumberInput(attrs={'type':'date'}),required=False)
    tags = forms.CharField(widget=forms.TextInput(
          attrs={'data-role':"taginput",'data-max-tags':"6",'data-random-color':"true"})
          ,required=False)

    class Meta:
        model = Project
        exclude = ['user']
        widgets = {
            'details': forms.Textarea(attrs={'rows': '5'}),
        }
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

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if Project.objects.filter(title=title).exists():
            self._update_errors(ValidationError({"title": "A project with this title already exists"}))

        return title

class ProjectFileForm(ProjectForm):
    file = MultipleFileField(widget=MultipleFileInput(attrs={'multiple': True}),required=False)

    # class Meta(ProjectForm.Meta):
    #     fields = ProjectForm.Meta.fields + ['file',]