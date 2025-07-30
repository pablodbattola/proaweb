from django.utils import timezone
from django.db import models

class Curso(models.Model):
    TURNOS = (
        (1, "Mañana"),
        (2, "Tarde"),
        (3, "Noche"),
    )

    nombre = models.CharField(max_length=128)
    inscriptos = models.IntegerField()
    solo_empresas = models.BooleanField(default=False)
    turno = models.IntegerField(choices=TURNOS, default=3)
    fecha_inicio = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nombre
