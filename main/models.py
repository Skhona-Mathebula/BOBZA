from django.db import models

# Create your models here.
class Wardrobe(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Shirt(models.Model):
    wardrobe = models.ForeignKey(Wardrobe, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    branded = models.BooleanField()

    def __str__(self):
        return self.text
