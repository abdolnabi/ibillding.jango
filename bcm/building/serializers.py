from building.models import (
    Residence, Facility, Unit, FacilityUnit, Block, UnitUser, BoardOfDirector,
    FacilityResidence, FacilityResidenceAccessibility
)
from core.serializers import CoreModelSerializer


class ResidenceSerializer(CoreModelSerializer):
    class Meta:
        model = Residence
        fields = ['parent_residence', 'manager', 'name', 'type', 'address', 'rules',
                  'appendix_to_statute', 'users_board']


class FacilitySerializer(CoreModelSerializer):
    class Meta:
        model = Facility
        fields = ['title', 'description', 'type', 'units']


class UnitSerializer(CoreModelSerializer):
    class Meta:
        model = Unit
        fields = ['residence', 'area', 'population', 'users']


class FacilityUnitSerializer(CoreModelSerializer):
    class Meta:
        model = FacilityUnit
        fields = ['unit', 'facility', 'second_title', 'description']


class BlockSerializer(CoreModelSerializer):
    class Meta:
        model = Block
        fields = ['residence', 'name', 'number_of_floors', 'number_of_units']


class UnitUserSerializer(CoreModelSerializer):
    class Meta:
        model = UnitUser
        fields = ['user', 'unit', 'type', 'confirmed']


class BoardOfDirectorSerializer(CoreModelSerializer):
    class Meta:
        model = BoardOfDirector
        fields = ['residence', 'user', 'role']


class FacilityResidenceSerializer(CoreModelSerializer):
    class Meta:
        model = FacilityResidence
        fields = ['residence', 'facility', 'second_title', 'description', 'requestable',
                  'price', 'blocks']


class FacilityResidenceAccessibilitySerializer(CoreModelSerializer):
    class Meta:
        model = FacilityResidenceAccessibility
        fields = ['facility_residence', 'type', 'accessible']
