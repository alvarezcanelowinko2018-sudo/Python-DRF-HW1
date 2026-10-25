from django.urls import path

from .views import PlayerListCreateView, PlayerRetrieveUpdateDestroyView

urlpatterns = [
    path('', PlayerListCreateView.as_view()),

    path('<int:pk>', PlayerRetrieveUpdateDestroyView.as_view()),
]