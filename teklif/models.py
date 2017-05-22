from django.db import models
from ilan.models import Ilan
from kullanici.models import IsArayan

class Teklif(models.Model):
    ilan = models.ForeignKey(Ilan,blank=True,null=True,related_name="odeme_ilanı")
    kullanici = models.ForeignKey(IsArayan,related_name="is_arayan")
    butce = models.IntegerField()
    sure = models.IntegerField()

    onay_durumu = models.BooleanField(default=False)
    teklif_tarihi = models.DateTimeField(auto_now_add=True)
    duzenlenme_tarihi = models.DateField(auto_now=True)

    def __str__(self):
        return self.ilan.ilan_basligi+ " ilanına "+ kullanici.kullanici.username + " kullanıcısının Teklifi"

    class Meta:
        verbose_name ="Teklifler"
        verbose_name_plural="Teklif"