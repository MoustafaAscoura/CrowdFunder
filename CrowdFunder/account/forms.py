from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class FullUserForm(UserChangeForm):
    password = None
    field_order = ['username','first_name','last_name','email']
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email']
