from django.contrib import admin
from projects.models import Project , Category , Donation

# Register your models here.

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Donation)