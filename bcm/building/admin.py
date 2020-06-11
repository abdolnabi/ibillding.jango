from django.contrib import admin
from building.models import (
    Residence,
    Facility,
    Unit,
    FacilityUnit,
    Block,
    UnitUser,
    BoardOfDirector,
    FacilityResidence,
    FacilityResidenceAccessibility,
    Location,
    UnitPhoneNumber,
    Budget,
    AccountingTarget,
    Bill,
    Advertisement,
    PaymentGateway,
    Payment,
)


class ResidenceAdmin(admin.ModelAdmin):
    list_display = ('manager', 'name', 'type', 'coordinate')
    list_filter = ('created',)


class FacilityAdmin(admin.ModelAdmin):
    list_display = ('title', 'type')
    list_filter = ('type',)


class UnitAdmin(admin.ModelAdmin):
    list_display = ('residence', 'population')
    list_filter = ('created',)


class UnitPhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('unit', 'phone')
    search_fields = ('phone',)


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


class BudgetAdmin(admin.ModelAdmin):
    list_display = ('title', 'period', 'budget_class', 'deadline_in_days', 'price')


class AccountingTargetAdmin(admin.ModelAdmin):
    list_display = ('content_type', 'object_id', )


class BillAdmin(admin.ModelAdmin):
    list_display = ('user', 'bill_class', 'type', 'price', 'currency', 'status')


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('type', 'status', 'image', 'link')


class PaymentGatewayAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('bill', 'payment_gateway', 'payer', 'status')


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
admin.site.register(UnitPhoneNumber, UnitPhoneNumberAdmin)
admin.site.register(Budget, BudgetAdmin)
admin.site.register(AccountingTarget, AccountingTargetAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(PaymentGateway, PaymentGatewayAdmin)
admin.site.register(Payment, PaymentAdmin)
