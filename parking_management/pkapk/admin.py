from django.contrib import admin
from .models import Category,add_vehicle

# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'parking_area_no', 'vehicle_type', 'vehicle_limit', 'parking_charge','status')
    list_display_links = ('id', 'parking_area_no')
    list_filter = ('vehicle_type', 'vehicle_limit')
    list_editable = ('status',)
    search_fields = ('parking_area_no',)
    ordering = ('vehicle_type', 'parking_area_no')


admin.site.register(Category, categoryAdmin)





admin.site.register(add_vehicle)
