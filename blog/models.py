from django.db import models


# Create your models here.

class User(models.Model):
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    date = models.DateField()
    email = models.EmailField()

    def __dir__(self):
        return self.password


class Reyting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ball = models.IntegerField(default=0)
    yangilangan_vaqt = models.DateTimeField(auto_now=True)
    daraja = models.CharField(max_length=20,
                              choices=[('Oltin', 'Oltin'),
                                       ('Kumush', 'Kumush'),
                                       ('Bronza', 'Bronza'),])

    def __str__(self):
        return f"{self.user} -( {self.ball} ball)"

class MockTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_nomi = models.CharField(max_length=255)
    natija = models.IntegerField()
    topshirilgan_vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - ({self.natija})"

class Universitet(models.Model):
    nomi = models.CharField(max_length=255)
    joylashuvi = models.CharField(max_length=255)
    reytingi = models.IntegerField()

    def __str__(self):
        return self.nomi

class Sozlamalar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    til = models.CharField(max_length=50, default="Uzbek")
    bildirishnoma_yoqilgan = models.CharField(max_length=15, default=True,
                                                 choices=[('Yes', 'Ha'),
                                                          ('Uzbek', 'Uzbek'),
                                                          ('Rus', 'Rus'),
                                                          ('English', 'English'),])

    def __str__(self):
        return f"Sozlamalar - {self.user}"

class Yutuq(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sarlavha = models.CharField(max_length=255)
    tavsif = models.TextField()
    erishilgan_sana = models.DateField()

    def __str__(self):
        return f"{self.user} - {self.sarlavha}"
