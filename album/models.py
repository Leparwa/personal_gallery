from django.db import models



class Location(models.Model):
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.location

class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category


class Image(models.Model):
    image = models.CharField(max_length=200)
    image_name = models.CharField(max_length=200)
    image_description = models.TextField(max_length=200)
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category, on_delete=models.CASCADE)