from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)
    picture = models.ImageField(upload_to='country_pics', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')
    picture = models.ImageField(upload_to='city_pics', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
