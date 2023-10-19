from django.urls import path,include,re_path
from .views import *

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('signup/', CreateAccount.as_view(), name='signup'),
    path('success/', Success, name='success'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('resend_mail/<str:uname>', ResendMail, name="resend_mail"),
    path('profile/<int:pk>', ShowProfile.as_view(), name='profile'),
    path('editprofile/<int:pk>', EditAccount.as_view(), name='editprofile'),
    path('profile/delete/<int:pk>', DeleteAccount.as_view(), name='delete_user'),
    path("logout/", Logout, name="logout"),
    path('', include('django.contrib.auth.urls')),
]

