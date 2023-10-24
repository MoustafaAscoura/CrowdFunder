from django import forms
from .models import Review,Report




class ReviewForm(forms.ModelForm):
    

    class Meta:
        model = Review
        fields = ['review','rate']



class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['reason','status']

    
