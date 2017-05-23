#! -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User 

class Hizmet(models.Model):
    hizmetAdi = models.CharField(max_length=50) 
    
    def __str__(self):
        return self.hizmetAdi

    class Meta:
        verbose_name ="Hizmet Türü"
        verbose_name_plural="Hizmet Türleri"


class HizmetDescription(models.Model):
    hizmetBasligi = models.CharField(max_length=50)
    hizmet = models.ForeignKey(Hizmet)
    yolMasrafi = models.BooleanField(default=True)
    yemekMasrafi = models.BooleanField(default=True)
    calismaTipleri = (
        ('U', 'Uzaktan'),
        ('A', 'Çalışma Alanında'),
    )
    calismaTipi = models.CharField(max_length=1, choices=calismaTipleri,blank=True, null=True)

    def hizmetSec(kategoriID):
        return HizmetDescription.objects.get(pk=kategoriID)
    
    def __str__(self):
        return self.hizmetBasligi

    class Meta:
        verbose_name ="Hizmet"
        verbose_name_plural="Hizmetler"

