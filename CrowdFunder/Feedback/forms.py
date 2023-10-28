from django import forms
from .models import *

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review','rate']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['content']

class ReplyForm(forms.ModelForm):
	class Meta:
		model = Reply
		fields = ['content']

class ReportForm(forms.ModelForm):
    status_ = (('Hateful Speech','Hateful Speech'),('Profanity', 'Profanity'),
                ('Abuse', 'Abuse'),('Violence','Violence'),
                ('Irrelevant','Irrelevant'))

    status = forms.ChoiceField(choices=status_)

    class Meta:
        model = Report
        fields = ['reason','status']

    
