from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register('person_list', views.PersonListView)
router.register('game_list', views.GameSessionView)

urlpatterns = [
    path('', include(router.urls)),
    path('create_person/', views.createPerson),
    path('create_game/', views.createGame),
    path('join_game/', views.joinGame),
    path('finish_game/', views.finishGame),
    path('leave_game/',views.leaveGame)
]
