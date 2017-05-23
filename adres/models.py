#! -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from kullanici.models import IsVeren

class Adres(models.Model):
    kullanici = models.ForeignKey(IsVeren,related_name="adres")
    adres_basligi = models.CharField(max_length=50)
    adres = models.CharField(max_length=80)
    sehir = models.CharField(max_length=40)
    ilce = models.CharField(max_length=40,blank=True, null=True)
    semt = models.CharField(max_length=40,blank=True, null=True)
    mahalle = models.CharField(max_length=40,blank=True, null=True)
    sokak = models.CharField(max_length=40,blank=True, null=True)
    no = models.CharField(max_length=10,blank=True, null=True)
    posta_kodu = models.CharField(max_length=40,blank=True, null=True)

    def __str__(self):
        return self.kullanici.kullanici.username + " " + self.adres_basligi

    class Meta:
        verbose_name ="İş Veren Adresi"
        verbose_name_plural="İş Veren Adresleri"

    def adresSec(adresID):
        return Adres.objects.get(pk=adresID)

    
