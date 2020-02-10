from django.contrib.auth import views as auth_views
from django.urls import path

from building.views import dashboard,residence_manage_page,new_residence_page,new_block_page,block_manage_page,unit_manage_page,new_unit_page,facility_manage_page,new_facility_page,delete_residence_page,delete_block_page,delete_unit_page,delete_facility_page

app_name = 'building'

urlpatterns = [
    #  Dashboard Paths =======================
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/residence/', residence_manage_page, name='residence_manage_page'),
    path('dashboard/residence/new/', new_residence_page, name='new_residence_page'),
    path('dashboard/residence/delete/', delete_residence_page, name='delete_residence_page'),
    ######## Block Path ############
    path('dashboard/block/', block_manage_page, name='block_manage_page'),
    path('dashboard/block/new/', new_block_page, name='new_block_page'),
    path('dashboard/block/delete/', delete_block_page, name='delete_block_page'),

    ######## Unit Path ############
    path('dashboard/unit/', unit_manage_page, name='unit_manage_page'),
    path('dashboard/unit/new/', new_unit_page, name='new_unit_page'),
    path('dashboard/unit/delete/', delete_unit_page, name='delete_unit_page'),

    ######## Unit Path ############
    path('dashboard/facility/', facility_manage_page, name='facility_manage_page'),
    path('dashboard/facility/new/', new_facility_page, name='new_facility_page'),
    path('dashboard/facility/delete/', delete_facility_page, name='delete_facility_page'),

    # path('dashboard/facility/delete/', delete_facility_page, name='new_facility_page'),
    # path('dashboard/facility/edit/', edit_facility_page, name='new_facility_page'),
]
