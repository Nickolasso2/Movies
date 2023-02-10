from dataclasses import fields
from socket import fromshare
from django import forms
from .models import Review, ReviewViaMptt, Rating, RatingStar

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('name', 'email', 'text')
        widgets = {'text':forms.Textarea(attrs={'cols':30})}

class ReviewFormMptt(forms.ModelForm):

    class Meta:
        model = ReviewViaMptt
        fields = ('name', 'email', 'text')


class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(queryset=RatingStar.objects.all(), widget=forms.RadioSelect)#RadioSelect - input type="radio"

    class Meta:
        model = Rating
        fields = ['star']
        


        