from django import forms

from building.models import Residence, Facility, Unit, FacilityUnit, Block, UnitUser, BoardOfDirector, \
    FacilityResidence, FacilityResidenceAccessibility


class ResidenceForm(forms.ModelForm):
    class Meta:
        model = Residence
        fields = ['type', 'name', 'parent_residence', 'manager', 'address', 'rules',
                  'appendix_to_statute', 'users_board']


class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['title', 'description', 'type', 'units']


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['residence', 'area', 'population', 'users']


class FacilityUnitForm(forms.ModelForm):
    class Meta:
        model = FacilityUnit
        fields = ['unit', 'facility', 'second_title', 'description']


class BlockForm(forms.ModelForm):
    class Meta:
        model = Block
        fields = ['residence', 'name', 'number_of_floors', 'number_of_units']


class UnitUserForm(forms.ModelForm):
    class Meta:
        model = UnitUser
        fields = ['user', 'unit', 'type', 'confirmed']


class BoardOfDirectorForm(forms.ModelForm):
    class Meta:
        model = BoardOfDirector
        fields = ['residence', 'user', 'role']


class FacilityResidenceForm(forms.ModelForm):
    class Meta:
        model = FacilityResidence
        fields = ['residence', 'facility', 'second_title', 'description', 'requestable',
                  'price', 'blocks']


class FacilityResidenceAccessibilityForm(forms.ModelForm):
    class Meta:
        model = FacilityResidenceAccessibility
        fields = ['facility_residence', 'type', 'accessible']
