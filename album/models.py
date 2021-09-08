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
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='locate')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='catego')

    def __str__(self):
        return self.name

    def save_photo(self):
        self.save()   

    @classmethod
    def search_image(cls,category):
        photos = cls.objects.filter(category__category__icontains = category)
        return photos

    @classmethod
    def filter_by_location(cls,location):
        photos = cls.objects.filter(location__location__icontains = location)
        return photos
    
    @classmethod
    def get_image_by_id(cls,id):
        photo = cls.objects.get(id = id)
        return photo


    