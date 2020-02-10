from django.shortcuts import render
from django.utils.translation import gettext
from django.utils import translation
from django.http import JsonResponse

############Dashboard Base section #######################

def dashboard(request):
    return render(request, 'dashboard_pages/dashboard_base.html')

############ Residence section #######################

def residence_manage_page(request):
    return render(request, 'dashboard_pages/residence/residence_managment.html')

def new_residence_page(request):
    return render(request, 'dashboard_pages/residence/new_residence.html')

def delete_residence_page(request):
    def get(self, request):
        id1 = request.GET.get('residence_id', None)
        # residence.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)
############ Block section #######################

def block_manage_page(request):
    return render(request, 'dashboard_pages/blocks/block_managment.html')

def new_block_page(request):
    return render(request, 'dashboard_pages/blocks/new_block.html')

def delete_block_page(request):
    def get(self, request):
        id1 = request.GET.get('block_id', None)
        # residence.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

############ Unit section #######################

def unit_manage_page(request):
    return render(request, 'dashboard_pages/units/unit_managment.html')

def new_unit_page(request):
    return render(request, 'dashboard_pages/units/new_unit.html')
def delete_unit_page(request):
    def get(self, request):
        id1 = request.GET.get('unit_id', None)
        # residence.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

############ Facility section #######################

def facility_manage_page(request):
    return render(request, 'dashboard_pages/facilities/facility_managment.html')

def new_facility_page(request):
    return render(request, 'dashboard_pages/facilities/new_facility.html')
def delete_facility_page(request):
    def get(self, request):
        id1 = request.GET.get('facility_id', None)
        # residence.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

