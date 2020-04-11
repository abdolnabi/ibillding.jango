from django.contrib.contenttypes.models import ContentType


residence = ContentType.objects.get(model='residence')
block = ContentType.objects.get(model='block')
unit = ContentType.objects.get(model='unit')

accounting_target_representation = {str(residence.id): 'residence',
                                    'residence': residence,
                                    str(block.id): 'block',
                                    'block': block,
                                    str(unit.id): 'unit',
                                    'unit': unit}

accounting_target_internal = {str(residence.id): residence,
                              'residence': residence,
                              str(block.id): block,
                              'block': block,
                              str(unit.id): unit,
                              'unit': unit}


def content_type_converter(key, mode, id=True):
    if mode == 'representation':
        data = accounting_target_representation[key]
        if isinstance(data, str):
            return data
        return data

    elif mode == 'internal':
        data = accounting_target_internal[key]
        if isinstance(data, str):
            return data
        if id:
            return data.id
        return data
