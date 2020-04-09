from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from core.services import content_type_converter


class CoreModelSerializer(serializers.ModelSerializer):
    pass


class ContentTypeField(serializers.CharField):
    default_error_messages = {
        'invalid': _('A valid content type is required.'),
    }

    def to_representation(self, value):
        if not value:
            return None

        return content_type_converter(str(value.id), mode='representation')

    def to_internal_value(self, data):
        data = super().to_internal_value(data=data)

        return content_type_converter(data, mode='internal')
