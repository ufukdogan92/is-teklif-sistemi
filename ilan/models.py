from django.db import models
from django.contrib.auth.models import User
from kullanici.models import IsVeren
from adres.models import Adres
from hizmet.models import HizmetDescription,Hizmet

class Ilan(models.Model):
    kullanici = models.ForeignKey(IsVeren,related_name="is_veren")
    hizmetDescr = models.ForeignKey(HizmetDescription,related_name="hizmet_descr")
    hizmet = models.ForeignKey(Hizmet,blank=True,null=True,related_name="hizmet_tipi")
    adres = models.ForeignKey(Adres,blank=True,null=True,related_name="is_veren_adresi")
    
    ilan_basligi = models.CharField(max_length=40)
    butceTipleri = (
        ('TL', 'Türk Lirası'),
        ('DLR', 'DOLAR'),
        ('EUR', 'EURO'),
    )
    sureUzunluklari = (
        ('S', 'Saat'),
        ('G', 'Gün'),
        ('A', 'Ay'),
        ('H', 'Hafta'),
        ('Y', 'Yıl'),
    )

    sureUzunlugu = models.CharField(max_length=3, choices=sureUzunluklari,default="G")
    sure = models.IntegerField()
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

    def adresSec(adresID):
        return Adres.objects.get(pk=adresID)

    def save(self, *args, **kwargs):
        
        from register.models import Register
        ilan = Register.ilanVermeBaslat()
        ilan = self
        ilan.kullanici = Register.getIsveren(self.kullanici.pk)
        ilan.hizmetDescr = Register.hizmetKategorisiSec(self.hizmetDescr.pk)
        ilan.adres = Ilan.adresSec(self.adres.pk)

        ilan.hizmet = ilan.hizmetDescr.hizmet
        ilan.ilan_basligi = self.ilan_basligi
        ilan.sureUzunlugu = self.sureUzunlugu
        ilan.sure = self.sure
        ilan.butceTipi = self.butceTipi
        ilan.butce = self.butce
        ilan.yayin_tarihi = self.yayin_tarihi
        ilan.duzenlenme_tarihi = self.duzenlenme_tarihi
        self = ilan
        
        super(Ilan, self).save(*args, **kwargs)