from django.contrib import admin
from building.models import (
    Residence, Facility, Unit, FacilityUnit, Block, UnitUser, BoardOfDirector,
    FacilityResidence, FacilityResidenceAccessibility,
    Location)


class ResidenceAdmin(admin.ModelAdmin):
    list_display = ('manager', 'name', 'type', 'coordinate')
    list_filter = ('created',)


class FacilityAdmin(admin.ModelAdmin):
    list_display = ('title', 'type')
    list_filter = ('type',)


class UnitAdmin(admin.ModelAdmin):
    list_display = ('residence', 'population')
    list_filter = ('created',)


class FacilityUnitAdmin(admin.ModelAdmin):
    list_display = ('unit', 'facility',)


class BlockAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_floors', 'number_of_units')
    list_filter = ('number_of_units', 'number_of_floors')


class UnitUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'unit', 'type', 'confirmed')
    list_filter = ('type', 'confirmed')


class BoardOfDirectorAdmin(admin.ModelAdmin):
    list_display = ('residence', 'user', 'role')
    list_filter = ('role',)


class FacilityResidenceAdmin(admin.ModelAdmin):
    list_display = ('residence', 'facility', 'requestable', 'price')
    list_filter = ('requestable',)


class FacilityResidenceAccessibilityAdmin(admin.ModelAdmin):
    list_display = ('facility_residence', 'type', 'accessible',)
    list_filter = ('type', 'accessible',)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude')


admin.site.register(FacilityResidenceAccessibility, FacilityResidenceAccessibilityAdmin)
admin.site.register(FacilityResidence, FacilityResidenceAdmin)
admin.site.register(BoardOfDirector, BoardOfDirectorAdmin)
admin.site.register(UnitUser, UnitUserAdmin)
admin.site.register(Block, BlockAdmin)
admin.site.register(FacilityUnit, FacilityUnitAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Residence, ResidenceAdmin)
admin.site.register(Location, LocationAdmin)
