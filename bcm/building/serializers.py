from rest_framework import serializers
import json
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
)
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


class ResidenceFacilityResidenceSerializer(CoreModelSerializer):
    class Meta:
        model = FacilityResidence
        fields = ['id', 'residence', 'facility', 'second_title', 'description', 'requestable',
                  'price', 'blocks']
        read_only_fields = ('residence',)


class ResidenceSerializer(CoreModelSerializer):
    facility_residences = ResidenceFacilityResidenceSerializer(many=True, required=False)
    coordinate = LocationSerializer()

    class Meta:
        model = Residence
        fields = ('id', 'parent_residence', 'manager', 'name', 'type', 'address', 'rules',
                  'appendix_to_statute', 'users_board', 'coordinate',
                  'facility_residences'
                  )

    def create(self, validated_data):
        coordinate_data = validated_data.pop('coordinate')
        request = self.context['request']
        facility_residenc = json.loads(request.data.get('facility_residences'))
        coordinate = dict()
        for key, value in coordinate_data.items():
            coordinate[key] = value
        coordinate = Location.objects.create(**coordinate)
        validated_data['coordinate'] = coordinate
        if facility_residenc != []:
            facility_residence_data = facility_residenc

            instance = super().create(validated_data)

            for facility_residence in facility_residence_data:
                item = dict()
                for key, value in facility_residence.items():
                    if key == 'facility':
                        facility_obj = Facility.objects.get(id=value)
                        item[key] = facility_obj
                    else:
                        item[key] = value

                if isinstance(item.get('blocks'), list):
                    del item['blocks']

                obj = FacilityResidence.objects.create(residence=instance, **item)
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
        validated_data.pop('facility_residences', [])
        instance = super().update(instance, validated_data)

        return instance


class BudgetSerializer(CoreModelSerializer):
    class Meta:
        model = Budget
        fields = ('id', 'title', 'budget_class', 'period', 'start_at', 'deadline_in_days', 'finish_at', 'due_at',
                  'price', 'price_formula', 'parameters')
