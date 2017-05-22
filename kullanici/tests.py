from django.test import TestCase
from .models import IsVeren
from django.contrib.auth.models import User 

class IsVerenTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="ufukdogan")
        IsVeren.objects.create(kullanici=user,cinsiyet='E',dogumGunu="1992-09-24",telefon="456456")

    def test_isVeren(self):
        ufukdogan = IsVeren.objects.get(kullanici=1)
        print (ufukdogan.kullanici.username)


