import re
from typing import Any
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
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
            if w > 400 or h > 400:
                self._update_errors(ValidationError({"picture": "Picture Dimensions must be 400*400 or less"}))

        return picture

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if self._meta.model.objects.filter(email__iexact=email).exists():
            self._update_errors(ValidationError({"email": "A user with this email already exists"}))
        else:
            return email
    

class FullUserForm(UserChangeForm):
    password = None
    field_order = ['username','first_name','last_name','email']
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email']
    

