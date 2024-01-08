from django import forms
from .models import Event, User

class EventForm(forms.ModelForm):
    datetime = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}))
    class Meta:
        model=Event
        exclude=["datetime"]


class UserForm(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    # events=forms.ModelMultipleChoiceField(Event.objects.all(),widget=forms.CheckboxSelectMultiple)

class eventRegisterForm(forms.Form):
    email=forms.EmailField()
    
