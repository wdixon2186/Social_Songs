from django import forms
from .models import Director, Video


class DirectorForm(forms.ModelForm):

    class Meta:
        model = Director
        fields = ('name', 'age', 'nationality', 'photo_url', 'thumb', 'films' ,)

class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ["name", "videofile"]
