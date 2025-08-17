from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='vehicles')
    name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=50, default='unknown')
    description = models.TextField(blank=True)
    daily_rate = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='vehicles/', blank=True, null=True)
    is_available = models.BooleanField(default=True)  # If you want to track availability

    def __str__(self):
        return self.name

class Rental(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    payment_method = models.CharField(max_length=20)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
