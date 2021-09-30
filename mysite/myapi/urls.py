from django.urls import include, path
from rest_framework import routers
from . import views
from django.contrib.auth.decorators import login_required

router = routers.DefaultRouter()
router.register(r'JUEGOS', views.JuegoViewSet)
router.register(r'PARTYS', views.PartyViewSet)
router.register(r'PARTY PLAYERS', views.PartyPlayersViewSet)
router.register(r'PARTYS CHAT', views.PartyChatViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
