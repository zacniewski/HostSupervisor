from django.db import models


class Vlan(models.Model):
    numer = models.CharField(max_length=30)
    uwagi = models.TextField(default='Brak', blank=True)

    class Meta:
        verbose_name_plural = 'Sieci VLAN'

    def __str__(self):
        return self.numer


class Host(models.Model):
    numer_vlan = models.ForeignKey(Vlan, on_delete=models.CASCADE)
    ip = models.CharField(max_length=30)
    nazwa_hosta = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Hosty'

    def __str__(self):
        return self.ip

