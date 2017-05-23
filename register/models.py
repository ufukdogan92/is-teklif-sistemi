from django.db import models
from ilan.models import Ilan
from kullanici.models import IsVeren,IsArayan
from hizmet.models import HizmetDescription
# Create your models here.

class Register(models.Model):
    def ilanVermeBaslat():
        ilan = Ilan()
        return ilan

    def getIsveren(kullaniciID):
        return IsVeren.getIsveren(kullaniciID)

    def hizmetKategorisiSec(kategoriID):
        return HizmetDescription.hizmetSec(kategoriID)

    def teklifVermeBaslat(ilanID):
        return Ilan.objects.get(pk=ilanID)

    def getIsArayan(kullaniciID):
        return IsArayan.getIsArayan(kullaniciID)
        
    
