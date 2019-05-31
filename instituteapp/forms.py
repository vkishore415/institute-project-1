from django import forms
from .import models

from multiselectfield import MultiSelectFormField
class FeedbackForm(forms.Form):
        name=forms.CharField(
            label='enter your name',
            widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'yourname'
                 }
             )
         )


        rating=forms.IntegerField(
            label='Enter your rating',
            widget=forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'your Rating'
                 }
             )
        )
        feedback=forms.CharField(
            label='Enter your feedback',
            widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'your Feedback'
                }
            )
        )





class ContactForm(forms.Form):
        name=forms.CharField(
            label='enter your name',
            widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'yourname'
                }
            )
        )

        email = forms.EmailField(
            label='enter your email',
            widget=forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'youremail'
                }
            )
        )
        mobile= forms.IntegerField(
            label='enter your number',
            widget=forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'yournumber'
                }
            )
        )

        LOCATION_CHOICES = (
            ('HYD', 'HYDERABAD'),
            ('PUNE', 'PUNE')
        )
        location=MultiSelectFormField(max_length=100,choices=LOCATION_CHOICES)
        COURSES_CHOICES = (
            ('PYTHON', 'PYTHON'),
            ('DJANGO', 'DJANGO')
        )
        courses = MultiSelectFormField(max_length=200, choices=COURSES_CHOICES)
        SHIFT_CHOICES = (
            ('MRNG', 'MORNING'),
            ('EVE', 'EVENING')
        )
        shifts =MultiSelectFormField(max_length=100, choices=SHIFT_CHOICES)
        start_date=forms.DateField(
            widget=forms.SelectDateWidget()
        )
        GENDER_CHOICES=(
            ('M','MALE'),
            ('F','FEMALE')
        )
        gender=forms.ChoiceField(
            widget=forms.RadioSelect(),choices=GENDER_CHOICES
        )