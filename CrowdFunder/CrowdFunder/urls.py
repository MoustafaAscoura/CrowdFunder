from django.contrib import admin
from django.urls import path , re_path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('projects.urls')),
    path('',include('home.urls')),
    re_path('account/',include('account.urls')),
    path('Feedback',include('Feedback.urls')),

]  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
