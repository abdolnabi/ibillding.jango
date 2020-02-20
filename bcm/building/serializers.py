from building.models import (
    Residence, Facility, Unit, FacilityUnit, Block, UnitUser, BoardOfDirector,
    FacilityResidence, FacilityResidenceAccessibility,
    Location)
from core.serializers import CoreModelSerializer


class LocationSerializer(CoreModelSerializer):
    class Meta:
        model = Location
        fields = ('latitude', 'longitude')


class FacilitySerializer(CoreModelSerializer):
    class Meta:
        model = Facility
        fields = ['id', 'title', 'description', 'type', 'units']


class UnitSerializer(CoreModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'residence', 'area', 'population', 'users']


class FacilityUnitSerializer(CoreModelSerializer):
    class Meta:
        model = FacilityUnit
        fields = ['id', 'unit', 'facility', 'second_title', 'description']


class BlockSerializer(CoreModelSerializer):
    class Meta:
        model = Block
        fields = ['id', 'residence', 'name', 'number_of_floors', 'number_of_units']


class UnitUserSerializer(CoreModelSerializer):
    class Meta:
        model = UnitUser
        fields = ['id', 'user', 'unit', 'type', 'confirmed']


class BoardOfDirectorSerializer(CoreModelSerializer):
    class Meta:
        model = BoardOfDirector
        fields = ['id', 'residence', 'user', 'role']


class FacilityResidenceSerializer(CoreModelSerializer):
    class Meta:
        model = FacilityResidence
        fields = ['id', 'residence', 'facility', 'second_title', 'description', 'requestable',
                  'price', 'blocks']


class FacilityResidenceAccessibilitySerializer(CoreModelSerializer):
    class Meta:
        model = FacilityResidenceAccessibility
        fields = ['id', 'facility_residence', 'type', 'accessible']


class ResidenceSerializer(CoreModelSerializer):
    facility_residence = FacilityResidenceSerializer(source='facility_residences', many=True)
    coordinate = LocationSerializer()

    class Meta:
        model = Residence
        fields = ['id', 'parent_residence', 'manager', 'name', 'type', 'address', 'rules',
                  'appendix_to_statute', 'users_board', 'coordinate', 'facility_residence']
