from django.shortcuts import render
from django.utils.translation import gettext
from django.utils import translation

############Dashboard Base section #######################

def dashboard(request):
    return render(request, 'dashboard_pages/dashboard_base.html')

############ Residence section #######################

def ResidenceManagePage(request):
    return render(request, 'dashboard_pages/residence/residence_managment.html')

def NewResidencePage(request):
    return render(request, 'dashboard_pages/residence/New_residence.html')

############ Block section #######################

def BlockManagePage(request):
    return render(request, 'dashboard_pages/Blocks/block_managment.html')

def NewBlockPage(request):
    return render(request, 'dashboard_pages/Blocks/New_block.html')

############ Unit section #######################

def UnitManagePage(request):
    return render(request, 'dashboard_pages/Units/unit_managment.html')

def NewUnitPage(request):
    return render(request, 'dashboard_pages/Units/New_unit.html')

############ Facility section #######################

def FacilityManagePage(request):
    return render(request, 'dashboard_pages/Facilities/Facility_managment.html')

def NewFacilityPage(request):
    return render(request, 'dashboard_pages/Facilities/New_Facility.html')

