from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets

# ###########Dashboard Base section #######################
from building.models import Residence, Facility, Unit, FacilityUnit, Block, UnitUser, BoardOfDirector, \
    FacilityResidence, FacilityResidenceAccessibility
from building.serializers import ResidenceSerializer, FacilitySerializer, UnitSerializer, FacilityUnitSerializer, \
    BlockSerializer, UnitUserSerializer, BoardOfDirectorSerializer, FacilityResidenceSerializer, \
    FacilityResidenceAccessibilitySerializer

def dashboard(request):
    return render(request, 'dashboard_pages/dashboard_base.html')


# ########### Residence section #######################

def residence_manage_page(request):
    response = {
        'data': Residence.objects.all(),
        'request_type': 'new'

    }
    return render(request, 'dashboard_pages/residence/residence_managment.html', response)


def new_residence_page(request):
    request_type = 'new'

    data = {
        'residences': Residence.objects.all(),
        'request_type': request_type
    }
    return render(request, 'dashboard_pages/residence/new_residence.html', data)


def edit_residence_page(request, id):
    request_type = 'edit'
    # if request.method == 'GET':
    residence = Residence.objects.filter(id=id).get()
    # item_type_dropdown = Residence.RESIDENCE_TYPE_CHOICES
    data = {
        'residences': Residence.objects.all(),
        'residence': Residence.objects.filter(id=id).get(),
        'facility': Residence.objects.filter(id=id).get(),
        'request_type': request_type,
        'id': id,
        # 'item_type_dropdown': item_type_dropdown
    }
    if request.method == 'PUT':
        serializer = ResidenceSerializer(residence, data=request.data)
        data = {}
        serializer.save()
        return JsonResponse(serializer.data)

    return render(request, 'dashboard_pages/residence/new_residence.html', data)


def show_residence_page(request, id):
    request_type = 'show'
    data = {
        'residences': Residence.objects.all(),
        'residence': Residence.objects.filter(id=id).get(),
        'request_type': request_type,
        'id': id,
    }
    return render(request, 'dashboard_pages/residence/new_residence.html', data)


def delete_residence_page(request):
        # id1 = request.GET.get('residence_id', None)
        # residence.objects.get(id=id1).delete()
    data = {
            'deleted': True
        }

    return JsonResponse(data)


############ Block section #######################

def block_manage_page(request):
    response = {
        'data': Block.objects.all(),
        'residences': Residence.objects.all(),
        'request_type': 'new'
    }
    return render(request, 'dashboard_pages/blocks/block_managment.html', response)


def new_block_page(request):
    request_type = 'new'
    data = {
        'residences': Residence.objects.all(),
        'request_type': request_type
    }
    return render(request, 'dashboard_pages/blocks/new_block.html', data)


def edit_block_page(request, id):
    request_type = 'edit'
    data = {
        'residences': Residence.objects.all(),
        'block_content': Block.objects.filter(id=id).get(),
        'request_type': request_type,
        'id': id,
        # 'item_type_dropdown': item_type_dropdown
    }
    return render(request, 'dashboard_pages/blocks/update_show_block.html', data)


# def update_block_page(request, id):
#     request_type = 'edit'
#     block = Block.objects.get(id=id)
#     if request.method == 'PUT':
#         serializer = BlockSerializer(block, data=request.content_params)
#         data = {}
#         if serializer.is_valid():
#             serializer.save()
#             data = "successful"
#             return JsonResponse(data=serializer.data)
#         else:
#             return JsonResponse(serializer.errors)
#         # return JsonResponse(serializer.data)
#     # item_type_dropdown = Residence.RESIDENCE_TYPE_CHOICES


def show_block_page(request, id):
    request_type = 'show'
    # item_type_dropdown = Residence.RESIDENCE_TYPE_CHOICES
    data = {
        'residences': Residence.objects.all(),
        'block_content': Block.objects.filter(id=id).get(),
        'request_type': request_type,
        'id': id,
        # 'item_type_dropdown': item_type_dropdown
    }
    return render(request, 'dashboard_pages/blocks/update_show_block.html', data)


# def delete_block_page(request,id):
#     id = request.GET.get('id')
#     # Block.objects.get(id=id1).delete()
#     data = {
#         'deleted': True,
#
#         }
#     return JsonResponse(data)


# ########### Unit section #######################

def unit_manage_page(request):
    response = {
        'data': Unit.objects.all(),
        'residences': Residence.objects.all(),
        'blocks': Block.objects.all(),
        'request_type': 'new'
    }
    return render(request, 'dashboard_pages/units/unit_managment.html', response)


def new_unit_page(request):
    request_type = 'new'
    data = {
        'residences': Residence.objects.all(),
        'blocks': Block.objects.all(),
        'request_type': request_type
    }
    return render(request, 'dashboard_pages/units/new_unit.html', data)


def edit_unit_page(request, id):
    request_type = 'edit'

    data = {
        'residences': Residence.objects.all(),
        'unit': Unit.objects.filter(id=id).get(),
        'request_type': request_type,
        'id': id,
        # 'item_type_dropdown': item_type_dropdown
    }
    return render(request, 'dashboard_pages/units/update_show_unit.html', data)


def show_unit_page(request, id):
    request_type = 'show'
    # item_type_dropdown = Residence.RESIDENCE_TYPE_CHOICES
    data = {
        'residences': Residence.objects.all(),
        'unit': Unit.objects.filter(id=id).get(),
        'request_type': request_type,
        'id': id,
        # 'item_type_dropdown': item_type_dropdown
    }
    return render(request, 'dashboard_pages/units/update_show_unit.html', data)

def delete_unit_page(request):
    def get(self, request):
        # id1 = request.GET.get('unit_id', None)
        # residence.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


# ########### Facility section #######################

def facility_manage_page(request):
    response = {
        'data': Facility.objects.all(),
        # 'residences': Residence.objects.all(),
        # 'blocks': Block.objects.all(),
        'request_type': 'new'
    }
    return render(request, 'dashboard_pages/facilities/facility_managment.html', response)


def new_facility_page(request):
    request_type = 'new'
    data = {
        'request_type': request_type
    }
    return render(request, 'dashboard_pages/facilities/new_facility.html', data)


def edit_facility_page(request, id):
    request_type = 'edit'

    data = {
        'facility': Facility.objects.filter(id=id).get(),
        'request_type': request_type,
        'id': id,
        # 'item_type_dropdown': item_type_dropdown
    }
    return render(request, 'dashboard_pages/facilities/update_show_facility.html', data)


def show_facility_page(request, id):
    request_type = 'show'
    # item_type_dropdown = Residence.RESIDENCE_TYPE_CHOICES
    data = {
        'facility': Facility.objects.filter(id=id).get(),
        'request_type': request_type,
        'id': id,
        # 'item_type_dropdown': item_type_dropdown
    }
    return render(request, 'dashboard_pages/facilities/update_show_facility.html', data)

def delete_facility_page(request):
    def get(self, request):
        # id1 = request.GET.get('facility_id', None)
        # residence.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)



# rest view section
class ResidenceViewSet(viewsets.ModelViewSet):
    queryset = Residence.objects.all()
    serializer_class = ResidenceSerializer


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class FacilityUnitViewSet(viewsets.ModelViewSet):
    queryset = FacilityUnit.objects.all()
    serializer_class = FacilityUnitSerializer


class BlockViewSet(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer


class UnitUserViewSet(viewsets.ModelViewSet):
    queryset = UnitUser.objects.all()
    serializer_class = UnitUserSerializer


class BoardOfDirectorViewSet(viewsets.ModelViewSet):
    queryset = BoardOfDirector.objects.all()
    serializer_class = BoardOfDirectorSerializer


class FacilityResidenceViewSet(viewsets.ModelViewSet):
    queryset = FacilityResidence.objects.all()
    serializer_class = FacilityResidenceSerializer


class FacilityResidenceAccessibilityViewSet(viewsets.ModelViewSet):
    queryset = FacilityResidenceAccessibility.objects.all()
    serializer_class = FacilityResidenceAccessibilitySerializer
