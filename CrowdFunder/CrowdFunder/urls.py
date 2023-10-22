from django.contrib import admin
from django.urls import path , re_path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('projects/',include('projects.urls')),
    path('accounts/',include('account.urls')),
    path('feedback/',include('Feedback.urls')),

]  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
