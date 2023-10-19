from django.urls import path,include
from .views import CreateAccount,EditAccount,ShowProfile,Logout,DeleteAccount,Login

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('signup/', CreateAccount.as_view(), name='signup'),
    path('profile/', ShowProfile, name='profile'),
    path('editprofile/<int:pk>', EditAccount.as_view(), name='editprofile'),
    path('profile/delete/<int:pk>', DeleteAccount.as_view(), name='delete_user'),
    path("logout/", Logout, name="logout"),
    path('', include('django.contrib.auth.urls')),
]

