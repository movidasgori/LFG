from django.contrib import admin
from .models import Juego
from .models import Party
from .models import PartyPlayers
from .models import PartyChat

# Register your models here.

admin.site.register(Juego)
admin.site.register(Party)
admin.site.register(PartyPlayers)
admin.site.register(PartyChat)


