from django.db import models
from ilan.models import Ilan
from teklif.models import Teklif

class Odeme(models.Model):
    odeme_basligi = models.CharField(max_length=40,blank=True,null=True)
    ucret = models.IntegerField(blank=True,null=True)
    sure = models.IntegerField(blank=True,null=True)
    teklif = models.ForeignKey(Teklif,blank=True,null=True,related_name="odeme_teklifi")


    odemeTurleri = (
        ('H', 'Havale'),
        ('N', 'Nakit'),
        ('O', 'Online Ödeme'),
    )

    odemeTuru = models.CharField(max_length=3, choices=odemeTurleri,default="N")
    tamamlanma_durumu = models.BooleanField(default=False)

    def __str__(self):
        return self.teklif.ilan.ilan_basligi + " Ödemesi"

    class Meta:
        verbose_name ="Ödeme"
        verbose_name_plural="Ödemeler"