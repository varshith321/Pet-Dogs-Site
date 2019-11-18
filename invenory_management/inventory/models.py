from django.db import models

# Create your models here.

photo = models.ImageField(upload_to="gallery")

class Place(models.Model):
    
    name = models.CharField(max_length=200, blank=False)
    place = models.CharField(max_length =200, blank = False)
    age = models.IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return 'Name: {0} Place: {1}'.format(self.name, self.place)

class Pup(Place):
    pass