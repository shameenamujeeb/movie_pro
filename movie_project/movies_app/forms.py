from django import forms

from .models import Movie, ReviewRating


class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['title', 'description', 'image' ,'release_date', 'actors' ,'language','genere','link']
class ReviewForm(forms.ModelForm):
    class Meta:
        model=ReviewRating
        fields=['review','rating']
        widgets={
            'review':forms.TextInput(attrs={'class':'form-control'}),
            'rating':forms.TextInput(attrs={'class':'form-control'}),
        }