from django.conf import settings
from django.db import models


# Create your models here.
# MODELO JUEGO
class Juego(models.Model):
    nombre = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.nombre


# MODELO PARTY
class Party(models.Model):
    nombre = models.ForeignKey(Juego, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion


# MODELO PARTYPLAYERS
class PartyPlayers(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    jugador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Restriccion para no repetir jugador en la PARTY
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['party', 'jugador'], name='jugador unico party')
        ]

    def __str__(self):
        return '{} - {}'.format(self.jugador, self.party)


# MODELO PARTYS CHAT
class PartyChat(models.Model):
    sala = models.ForeignKey(Party, on_delete=models.CASCADE)
    jugador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=200)

    def __str__(self):
        return '{} - {} - {}'.format(self.sala, self.jugador, self.comentario)
