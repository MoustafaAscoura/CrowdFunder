from django import forms
from .models import Review,Report, Comment




class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review','rate']




class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ['content']




class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['reason','status']

    
