from django.urls import path,include
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    #User functions
    path('profile/<int:pk>', ShowProfile.as_view(), name='profile'),
    path('profile/edit', login_required(EditAccount.as_view()), name='editprofile'),
    path('profile/delete', login_required(DeleteAccount.as_view()), name='delete_user'),

    #Authentication
    path('login/', Login.as_view(), name='login'),
    path('signup/', CreateAccount.as_view(), name='signup'),
    path('success/', Success, name='success'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('resend_mail/<str:uname>', ResendMail, name="resend_mail"),
    path("logout/", login_required(Logout), name="logout"),

    #Imports
    path('', include('django.contrib.auth.urls')),
    path('oauth/', include('social_django.urls'),name='social')
]

