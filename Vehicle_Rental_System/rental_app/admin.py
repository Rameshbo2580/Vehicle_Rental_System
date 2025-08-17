from django.contrib import admin
from .models import Vehicle, Rental, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'daily_rate', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('name',)

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'start_date', 'end_date', 'payment_method', 'total_price', 'timestamp')
    list_filter = ('payment_method', 'start_date')
    date_hierarchy = 'start_date'
