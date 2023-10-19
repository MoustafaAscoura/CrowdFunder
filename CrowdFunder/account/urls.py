from django.urls import path,include
from .views import *

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('signup/', CreateAccount.as_view(), name='signup'),
    path('success/', Success, name='success'),
    path('token' , token_send , name='token_send'),
    path('error' , error_page , name='error'),
    path('verify/<auth_token>' , verify ,name = "verify"),
    
    path('profile/<int:pk>', ShowProfile.as_view(), name='profile'),
    path('editprofile/<int:pk>', EditAccount.as_view(), name='editprofile'),
    path('profile/delete/<int:pk>', DeleteAccount.as_view(), name='delete_user'),
    path("logout/", Logout, name="logout"),
    path('', include('django.contrib.auth.urls')),
]

