from django.shortcuts import render
from django.utils.translation import gettext
from django.utils import translation

############Dashboard Base section #######################

def dashboard(request):
    return render(request, 'dashboard/dashboard_base.html')

############ Residence section #######################

def ResidenceManagePage(request):
    return render(request, 'dashboard/residence/residence_managment.html')

def NewResidencePage(request):
    return render(request, 'dashboard/residence/New_residence.html')

############ Block section #######################

def BlockManagePage(request):
    return render(request, 'dashboard/Blocks/block_managment.html')

def NewBlockPage(request):
    return render(request, 'dashboard/Blocks/New_block.html')

############ Unit section #######################

def UnitManagePage(request):
    return render(request, 'dashboard/Units/unit_managment.html')

def NewUnitPage(request):
    return render(request, 'dashboard/Units/New_unit.html')

############ Facility section #######################

def FacilityManagePage(request):
    return render(request, 'dashboard/Facilities/Facility_managment.html')

def NewFacilityPage(request):
    return render(request, 'dashboard/Facilities/New_Facility.html')

