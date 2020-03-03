from rest_framework import serializers

from building.models import (
    Residence, Facility, Unit, FacilityUnit, Block, UnitUser, BoardOfDirector,
    FacilityResidence, FacilityResidenceAccessibility,
    Location, UnitPhoneNumber)
from core.serializers import CoreModelSerializer


class LocationSerializer(CoreModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'latitude', 'longitude')


class FacilitySerializer(CoreModelSerializer):
    class Meta:
        model = Facility
        fields = ['id', 'title', 'description', 'type', 'units']


class UnitSerializer(CoreModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'residence', 'area', 'population', 'users']


class UnitPhoneNumberSerializer(CoreModelSerializer):
    class Meta:
        model = UnitPhoneNumber
        fields = ['id', 'unit', 'phone', 'description']


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
    id = serializers.IntegerField(required=False)

    class Meta:
        model = FacilityResidence
        fields = ['id', 'residence', 'facility', 'second_title', 'description', 'requestable',
                  'price', 'blocks']


class FacilityResidenceAccessibilitySerializer(CoreModelSerializer):
    class Meta:
        model = FacilityResidenceAccessibility
        fields = ['id', 'facility_residence', 'type', 'accessible']


class ResidenceSerializer(CoreModelSerializer):
    facility_residences = FacilityResidenceSerializer(many=True,required=False)
    coordinate = LocationSerializer()

    class Meta:
        model = Residence
        fields = ['id', 'parent_residence', 'manager', 'name', 'type', 'address', 'rules',
                  'appendix_to_statute', 'users_board', 'coordinate',
                  'facility_residences'
                  ]

    def create(self, validated_data):
        coordinate_data = validated_data.pop('coordinate')
        coordinate = dict()
        for key, value in coordinate_data.items():
            coordinate[key] = value
        coordinate = Location.objects.create(**coordinate)
        validated_data['coordinate'] = coordinate
        if 'facility_residences' in validated_data.keys():
        #     facility_residence_data = validated_data.pop('facility_residences')
        #     facility_residence_data = True
            facility_residence_data = validated_data.pop('facility_residences')

            instance = super().create(validated_data)

            for facility_residence in facility_residence_data:
                item = dict()
                for key, value in facility_residence.items():
                    item[key] = value

                if isinstance(item.get('blocks'), list):
                    del item['blocks']

                obj = FacilityResidence.objects.create(**item)
                instance.facility_residences.add(obj)

            instance.save()
        else:
            instance = super().create(validated_data)
            instance.save()

        return instance

    def update(self, instance, validated_data):
        coordinate_data = validated_data.pop('coordinate', {})
        for key, value in coordinate_data.items():
            setattr(instance.coordinate, key, value)
        instance.coordinate.save()
        if 'facility_residences' in validated_data.keys():

            facility_residence_data = validated_data.pop('facility_residences')

            facility_residences_data_ids = list()
            for item in facility_residence_data:
                if item.get('id'):
                    facility_residences_data_ids.append(item.get('id'))

            facility_residences_obj_ids = set(instance.facility_residences.values_list('id', flat=True))
            facility_residences_ids = facility_residences_obj_ids.difference(set(facility_residences_data_ids))
            FacilityResidence.objects.filter(id__in=facility_residences_ids).delete()
            instance.save()
            instance = super().update(instance, validated_data)

            for facility_residence in facility_residence_data:
                item = dict()
                for key, value in facility_residence.items():
                    item[key] = value

                if isinstance(item.get('blocks'), list):
                    del item['blocks']
                success = True
                if item.get('id'):
                    id = item.pop('id')
                    queryset = FacilityResidence.objects.filter(id=id)
                    success = not queryset.update(**item)
                    obj = queryset.first()
                    instance.facility_residences.add(obj)
                elif success:
                    obj = FacilityResidence.objects.create(**item)
                    instance.facility_residences.add(obj)

            instance.save()
        else:
            instance = super().create(validated_data)
            instance.save()
        return instance
