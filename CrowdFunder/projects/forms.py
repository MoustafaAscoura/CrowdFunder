from datetime import datetime
from typing import Any
from django import forms
from . models import Project , Category

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_time')
        end_date = cleaned_data.get('end_time')
        today_date = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")

        if today_date.date() > end_date.date():
            msg = "End date should be greater than Current date [ Should be after today !]."
            self._errors["end_time"] = self.error_class([msg])
        else:
            if end_date <= start_date:
                msg = "End date should be greater than start date."
                self._errors["end_time"] = self.error_class([msg])


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'
