from django.db import models
from django.contrib.auth.models import User
from kullanici.models import IsVeren
from adres.models import Adres

class Ilan(models.Model):
    kullanici = models.ForeignKey(IsVeren,related_name="is_veren")
    adres = models.ForeignKey(Adres,blank=True,null=True,related_name="is_veren_adresi")
    
    ilan_basligi = models.CharField(max_length=40)
    sure = models.IntegerField()
    butceTipleri = (
        ('TL', 'Türk Lirası'),
        ('DLR', 'DOLAR'),
        ('EUR', 'EURO'),
    )

    butceTipi = models.CharField(max_length=3, choices=butceTipleri,default="TL")
    butce = models.IntegerField()
    yayin_tarihi = models.DateTimeField(auto_now_add=True)
    duzenlenme_tarihi = models.DateField(auto_now=True)
    
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.ilan_basligi

    class Meta:
        verbose_name ="İlan"
        verbose_name_plural="İlanlar"