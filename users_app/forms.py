from django import forms
from .models import Profile,Education,WorkExperience

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Select the Author'}),

            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Price'})
        }






class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model=WorkExperience
        fields='__all__'

        widgets = {
            'start_date': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                      }),

            'end_date': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                      }),
        }



class EducationForm(forms.ModelForm):
    class Meta:
        model= Education
        fields ='__all__'