from django.db import models
from django.contrib import admin


class Provincia(models.Model):
    nombre = models.CharField(max_length=50)
    deficit_hab = models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=10)

    def __unicode__(self):
        return self.nombre


class ProvinciaPorAnio(models.Model):
    class Meta:
        unique_together = (("provincia", "anio"),)

    CHOICES_AFINIDAD = ((1, 1), (2, 2), (3, 3), )
    CHOICES_ANIO = ((2006, 2006), (2007,2007), (2008, 2008), (2009, 2009), (2010,2010), (2011,2011), (2012,2012), (2013,2013))

    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT)
    anio = models.IntegerField(choices=CHOICES_ANIO)
    afinidad = models.IntegerField(choices=CHOICES_AFINIDAD, null=True)
    cant_viviendas = models.IntegerField(null=True)
    monto = models.BigIntegerField(null=True)

    def __unicode__(self):
        return self.provincia.nombre + ' - ' + unicode(self.anio)

admin.site.register(Provincia)
admin.site.register(ProvinciaPorAnio)
