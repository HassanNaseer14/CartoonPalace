from django.urls import path 
from .views import CartoonListView, CartoonSeasonView, SeasonDetailView, EpisodeDetailView


urlpatterns = [
    path('', CartoonListView.as_view(), name="home"),
    #the url that shows the list of cartoon seasons
    path('cartoon/<int:pk>' , CartoonSeasonView.as_view(), name="cartoon"),

    #the url that i want to show the season details as well as the episodes associated with the season
    path('episode_list/<int:pk>' , SeasonDetailView.as_view(), name="episode_list"),

    #the url that shows the actual episode of the cartoon / season 
    path('episodes/<int:pk>' , EpisodeDetailView.as_view(), name="episodes"),
    
 
]