from django.contrib import admin

# Register your models here.
from .models import HizmetDescription,Hizmet
admin.site.register(Hizmet)
admin.site.register(HizmetDescription)
