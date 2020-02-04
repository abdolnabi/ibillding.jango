from django.contrib.auth import views as auth_views
from django.urls import path

from building.views import dashboard,ResidenceManagePage,NewResidencePage,NewBlockPage,BlockManagePage,UnitManagePage,NewUnitPage,FacilityManagePage,NewFacilityPage

app_name = 'building'

urlpatterns = [
    #  Dashboard Paths =======================
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/residence', ResidenceManagePage, name='ResidenceManagePage'),
    path('dashboard/residence/new', NewResidencePage, name='NewResidencePage'),
    ######## Block Path ############
    path('dashboard/block', BlockManagePage, name='BlockManagePage'),
    path('dashboard/block/new', NewBlockPage, name='NewBlockPage'),
    ######## Unit Path ############
    path('dashboard/unit', UnitManagePage, name='UnitManagePage'),
    path('dashboard/unit/new', NewUnitPage, name='NewUnitPage'),
    ######## Unit Path ############
    path('dashboard/facility', FacilityManagePage, name='FacilityManagePage'),
    path('dashboard/facility/new', NewFacilityPage, name='NewFacilityPage'),
]
