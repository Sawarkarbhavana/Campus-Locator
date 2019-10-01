from django.contrib import admin
from map.models import Building, Department

class ChoiceInline(admin.TabularInline):
    model = Department
    extra = 2

class BuildingAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    fieldsets = [
        ('Details', {
            'fields': ('name', 'description', 'image')
        }),
        ('Map coordinates of the building', {
            'fields': ('lat','long')
        })
    ]

admin.site.register(Building,BuildingAdmin)
admin.site.register(Department)