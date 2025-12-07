from django import forms


from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import TextInput, FileInput, NumberInput, Textarea


from django.contrib.auth.models import User
from .models import UserProfile
from .models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'description', 'location', 'image', 'phone_number', 'email']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Company name'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Short description', 'rows':3}),
            'location': TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'phone_number': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic', 'bio']
        
        widgets ={
            'profile_pic': FileInput(attrs={'class': 'input', 'placeholder': 'Profile Picture'}),
            'bio': TextInput(attrs={'class': 'input', 'placeholder': 'Update Bio'}),
        }
        
        
class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('email',)
        
        