import datetime
from django.utils import timezone
from django.db import models

# Create your models here.


class Batch(models.Model):
    type_choices = (
        ('1', 'ARABIGO'),
        ('2', 'ROBUSTA')
    )
    code = models.TextField()
    contact_name = models.TextField(default="")
    contact = models. TextField(default="")
    weight = models.FloatField()
    coffe_type = models.CharField(max_length=15,
                                  choices=type_choices)
    varieties = models.TextField()
    features = models.TextField()
    history_recoleccion = models.TextField(default={})
    history_despulpado = models.TextField(default={})
    history_fermentacion = models.TextField(default={})
    history_lavado = models.TextField(default={})
    history_secado = models.TextField(default={})
    history_trillado = models.TextField(default={})
    history_almacenado = models.TextField(default={})
    history_tostado = models.TextField(default={})
    history_etiquetado = models.TextField(default={})
    state = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    update_date = models.DateTimeField(
        default=timezone.now)
