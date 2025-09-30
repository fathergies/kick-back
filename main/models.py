import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('JERSEY', 'Jersey'),
        ('SHORTS', 'Celana / Shorts'),
        ('SHOES', 'Sepatu Bola / Futsal'),
        ('GEAR', 'Aksesoris (Sarung Tangan, Shin Guard, dll)'),
        ('MERCH', 'Merchandise / Collectibles'),
        ('OTHERS', 'Lain-lain'),
    ]
    
    name = models.CharField(max_length=255)
    specification = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Jersey')
    is_featured = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name
    


