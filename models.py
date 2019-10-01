from django.db import models

# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    lat = models.FloatField('Latitude coordinate',help_text="Refer the link : http://itouchmap.com/latlong.html")
    long = models.FloatField('Longitude coordinate')
    
    def __unicode__(self):
        return self.name
    
class Department(models.Model):
    building = models.ForeignKey(Building)
    name = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    initials = models.CharField(max_length=3, help_text="To be written in CAPS. Max 3 letters.")
    
    def __unicode__(self):
        return self.name
   
#class BuildingImages(models.Model):
#    building = models.ForeignKey(Building, related_name='images')
#    image = models.ImageField(upload_to = "images/")