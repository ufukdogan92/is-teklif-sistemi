from django.contrib import admin

# Register your models here.
from .models import Hizmet,HizmetDescription
admin.site.register(Hizmet)
admin.site.register(HizmetDescription)
