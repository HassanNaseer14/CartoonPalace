


# Create your models here.
from django.db import models

# Create your models here.

class Cartoon(models.Model):
    name = models.CharField(max_length=200)
    cover = models.URLField(max_length=300, blank=True, null=True)
    description = models.TextField()
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 


class CartoonSeason(models.Model):
    cartoon = models.ForeignKey(Cartoon, null=True, on_delete=models.CASCADE)
    number = models.IntegerField()
    season_cover = models.URLField(max_length=300, blank=True, null=True)
    season_name = models.CharField(max_length=200, blank=True, null=True)
    season_description = models.TextField(blank=True, null=False)
    
  
  
    def __str__(self):
        return self.cartoon.name + " | " +  str(self.season_name)


class Episode(models.Model):
    season = models.ForeignKey(CartoonSeason, on_delete=models.CASCADE)
    number = models.IntegerField()
    cover  = models.URLField(max_length=300, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=False)
    link = models.URLField(max_length=300, blank=True, null=True)
    published = models.DateField(auto_now_add=True, blank=True, null=True)


    class Meta:
        ordering = ["number"]
    def __str__(self):
        return str(self.number) + ": " +  self.name + " | " +  self.season.season_name +  " | " + self.season.cartoon.name

