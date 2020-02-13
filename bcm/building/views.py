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
    return render(request, 'dashboard_pages/residence/residence_managment.html')


def new_residence_page(request):
    return render(request, 'dashboard_pages/residence/new_residence.html')


def delete_residence_page(request):
    def get(self, request):
        # id1 = request.GET.get('residence_id', None)
        # residence.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


# ########### Block section #######################

def block_manage_page(request):
    return render(request, 'dashboard_pages/blocks/block_managment.html')


def new_block_page(request):
    return render(request, 'dashboard_pages/blocks/new_block.html')


def delete_block_page(request):
    def get(self, request):
        # id1 = request.GET.get('block_id', None)
        # residence.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


# ########### Unit section #######################

def unit_manage_page(request):
    return render(request, 'dashboard_pages/units/unit_managment.html')


def new_unit_page(request):
    return render(request, 'dashboard_pages/units/new_unit.html')


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
    return render(request, 'dashboard_pages/facilities/facility_managment.html')


def new_facility_page(request):
    return render(request, 'dashboard_pages/facilities/new_facility.html')


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
