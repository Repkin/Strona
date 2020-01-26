from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=128,default="")
    description = models.TextField(default="")
    year = models.IntegerField(null=True, blank=True)
    released = models.DateTimeField(null=True, blank=True)
    imbd_rating = models.DecimalField(null=True,blank=True,decimal_places=1,max_digits=3)

    def __str__(self):
        return self.name_with_year()

    def name_with_year(self):
        return str(self.name) + " (" +str(self.year) + " )"
# Create your models here.
