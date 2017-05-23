from django.db import models
from ilan.models import Ilan
from kullanici.models import IsArayan
from register.models import Register

class Teklif(models.Model):
    ilan = models.ForeignKey(Ilan,blank=True,null=True,related_name="odeme_ilanı")
    teklif_veren = models.OneToOneField(IsArayan,related_name="is_arayan")
    butce = models.IntegerField()
    sure = models.IntegerField()
    
    onay_durumu = models.BooleanField(default=False)
    teklif_tarihi = models.DateTimeField(auto_now_add=True)
    duzenlenme_tarihi = models.DateField(auto_now=True)

    def __str__(self):
        return self.ilan.ilan_basligi+ " ilanına "+ self.teklif_veren.kullanici.username + " kullanıcısının Teklifi"

    class Meta:
        verbose_name ="Teklifler"
        verbose_name_plural="Teklif"
    
    def save(self, *args, **kwargs):
        from register.models import Register
        self.ilan = Register.teklifVermeBaslat(self.ilan.pk)
        self.teklif_veren = Register.getIsArayan(self.teklif_veren.pk)
        super(Teklif, self).save(*args, **kwargs)
    

class TeklifOnay(models.Model):
    teklif = models.OneToOneField(Teklif,related_name="teklif_onay")

    onay_durumu = models.BooleanField(default=True)
    onay_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.teklif.ilan.ilan_basligi+ " ilanına verilen teklifin onayı"

    class Meta:
        verbose_name ="Teklif Onayı"
        verbose_name_plural="Teklif Onayları"

    def save(self, *args, **kwargs):
        if not self.pk:
            from odeme.models import Odeme
            teklif = Teklif.objects.get(pk=self.teklif.pk)
            self.onay_durumu = True
            self.tarihi = self.onay_tarihi
            odeme = Odeme(odeme_basligi=teklif.ilan.ilan_basligi,ucret=teklif.butce,sure=teklif.sure,teklif=teklif)
            odeme.save()
        super(TeklifOnay, self).save(*args, **kwargs)