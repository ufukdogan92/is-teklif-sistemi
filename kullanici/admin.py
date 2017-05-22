from django.contrib import admin

# Register your models here.
from .models import IsArayan,IsVeren
from adres.models import Adres

admin.site.register(IsArayan)

 
class IsVerenInline(admin.StackedInline):
    model = Adres 

class ExtendedVendorAdmin(admin.ModelAdmin):
    inlines = (IsVerenInline,)

  
admin.site.register(IsVeren,ExtendedVendorAdmin)