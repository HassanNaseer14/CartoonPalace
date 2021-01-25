from django.shortcuts import render
from django.http import HttpResponse
from  django.views.generic import ListView, DetailView
from .models import CartoonSeason, Cartoon, Episode
# Create your views here 

class CartoonListView(ListView):
    model = Cartoon
    template_name = "index.html"



class CartoonSeasonView(DetailView):
  
    model = Cartoon
    template_name = "season.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["seasons"] = CartoonSeason.objects.filter(cartoon=self.object)
        return context



class SeasonDetailView(DetailView):
  
    model = CartoonSeason
    template_name = "episode_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["episodes"] = Episode.objects.filter(season=self.object)
        return context



class EpisodeDetailView(DetailView):
  
    model = Episode
    template_name = "episode.html"