from django.contrib import admin
from building.models import (Residences, Facilities, Unit, FacilityUnit, Block, UnitUser, BoardOfDirectors,
                             FacilityResidence, FacilityResidenceAccessabilities)


class ResidencesAdmin(admin.ModelAdmin):
    list_display = ('manager', 'name', 'type',)
    list_filter = ('created',)


class FacilitiesAdmin(admin.ModelAdmin):
    list_display = ('title', 'type')
    list_filter = ('type',)


class UnitAdmin(admin.ModelAdmin):
    list_display = ('residences', 'population')
    list_filter = ('created',)


class FacilityUnitAdmin(admin.ModelAdmin):
    list_display = ('unit', 'facility',)


class BlockAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_floors', 'number_of_units')
    list_filter = ('number_of_units', 'number_of_floors')


class UnitUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'unit', 'type', 'confirmed')
    list_filter = ('type', 'confirmed')


class BoardOfDirectorsAdmin(admin.ModelAdmin):
    list_display = ('residence', 'user', 'role')
    list_filter = ('role',)


class FacilityResidenceAdmin(admin.ModelAdmin):
    list_display = ('residence', 'facility', 'requestable', 'price')
    list_filter = ('requestable',)


class FacilityResidenceAccessabilitiesAdmin(admin.ModelAdmin):
    list_display = ('facility_residence', 'type', 'accessible',)
    list_filter = ('type', 'accessible',)


admin.site.register(FacilityResidenceAccessabilities, FacilityResidenceAccessabilitiesAdmin)
admin.site.register(FacilityResidence, FacilityResidenceAdmin)
admin.site.register(BoardOfDirectors, BoardOfDirectorsAdmin)
admin.site.register(UnitUser, UnitUserAdmin)
admin.site.register(Block, BlockAdmin)
admin.site.register(FacilityUnit, FacilityUnitAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Facilities, FacilitiesAdmin)
admin.site.register(Residences, ResidencesAdmin)
