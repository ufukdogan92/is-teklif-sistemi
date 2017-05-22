#! -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User 
import datetime
from django.db.models.signals import post_save
from HizmetMapper.models import Hizmet


class IsVeren(models.Model):
    kullanici = models.ForeignKey(User,related_name="is_veren")
    cinsiyetSecenekleri = (
        ('E', 'Erkek'),
        ('K', 'Kadın'),
    )
    cinsiyet = models.CharField(max_length=1, choices=cinsiyetSecenekleri,blank=True, null=True)
    dogumGunu = models.DateField(blank=True, null=True,default=datetime.date.today)
    telefon = models.CharField(max_length=12,blank=True, null=True)
    fotograf = models.ImageField(blank=True, null=True,upload_to="users")
    
    def __str__(self):
        return self.kullanici.username

    class Meta:
        verbose_name ="İş Veren Profili"
        verbose_name_plural="İş Veren Profilleri"

class IsArayan(models.Model):
    kullanici = models.ForeignKey(User,related_name="is_arayan")
    hizmetler = models.ManyToManyField(Hizmet,related_name="hizmetler")
    CinsiyetSecenekleri = (
        ('E', 'Erkek'),
        ('K', 'Kadın'),
    )
    ISARAYANTIPI = (
        ('S', 'Şirket'),
        ('B', 'Bireysel'),
    )
    cinsiyet = models.CharField(max_length=1, choices=CinsiyetSecenekleri,blank=True, null=True)
    isArayanTipi = models.CharField(max_length=1, choices=ISARAYANTIPI,blank=True, null=True)
    dogumGunu = models.DateField(blank=True, null=True,default=datetime.date.today)
    telefon = models.CharField(max_length=12,blank=True, null=True)
    fotograf = models.ImageField(blank=True, null=True,upload_to="kullanicilar")

    
    def __str__(self):
        return self.kullanici.username

    class Meta:
        verbose_name ="İş Arayan Profili"
        verbose_name_plural="İş Arayan  Profilleri"