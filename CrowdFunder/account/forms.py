import re
from typing import Any
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserChangeForm, UserCreationForm,AuthenticationForm
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.forms.widgets import NumberInput

from django import forms
from .models import User


class CreateUserForm(UserCreationForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    class Meta:
        model=User
        fields = ['username','first_name','last_name','email','password1','password2','phone','picture']

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        re.compile('^01[0125]{1}[0-9]{8}$')
        if re.fullmatch('^01[0125]{1}[0-9]{8}$',phone):
            return phone
        else:
            self._update_errors(ValidationError({"phone": "Phone must match Egyptian format"}))
    
    def clean_picture(self):
        picture = self.cleaned_data.get("picture")
        
        if picture:
            w, h = get_image_dimensions(picture)
            if w > 800 or h > 800:
                self._update_errors(ValidationError({"picture": "Picture Dimensions must be 800*800 or less"}))
                
        return picture

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if self._meta.model.objects.filter(email__iexact=email).exists():
            self._update_errors(ValidationError({"email": "A user with this email already exists"}))
        else:
            return email
    
class LoginForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                try:
                    user_temp = User.objects.get(username=username)
                except:
                    raise self.get_invalid_login_error()
                if not user_temp.is_active:
                    raise forms.ValidationError("verify-"+username)
            else:
                self.confirm_login_allowed(self.user_cache)
            
            return self.cleaned_data

class FullUserForm(UserChangeForm):
    password = None
    email = forms.EmailField(disabled=True,required=False)
    birthdate = forms.DateTimeField(widget=NumberInput(attrs={'type':'date'}),required=False)
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email','phone','birthdate','profile','country']
        labels = {
            "profile": "Social Media URL"
        }
    
    def clean_email(self):
        return self.instance.email
            
    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        re.compile('^01[0125]{1}[0-9]{8}$')
        if phone and not re.fullmatch('^01[0125]{1}[0-9]{8}$',phone) :
            self._update_errors(ValidationError({"phone": "Phone must match Egyptian format"}))

        return phone
    
    def clean_picture(self):
        picture = self.cleaned_data.get("picture")
        if picture:
            w, h = get_image_dimensions(picture)
            if w > 800 or h > 800:
                self._update_errors(ValidationError({"picture": "Picture Dimensions must be 800*800 or less"}))

        return picture

