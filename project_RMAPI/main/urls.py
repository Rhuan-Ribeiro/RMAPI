from django.urls import path
from .views import *

urlpatterns = [
    path('character/', CharacterAPIView.as_view(), name="character"),
    path('character/<int:characterId>', CharacterAPIView.as_view(), name="characterById"),
    path('location/', LocationAPIView.as_view(), name="location"),
    path('location/<int:locationId>', LocationAPIView.as_view(), name="locationById"),
    path('episode/', EpisodeAPIView.as_view(), name="episode"),
    path('episode/<int:epId>', EpisodeAPIView.as_view(), name="episodeById"),
    path('character_episode/', EpisodeAPIView.as_view(), name="character_episode"),
    path('character_episode/<int:chracter_epId>', EpisodeAPIView.as_view(), name="character_episodeById"),
]