from django.urls import path, include
from rest_framework.routers import DefaultRouter

from building.views import (
    dashboard, residence_manage_page, new_residence_page, new_block_page, block_manage_page,
    unit_manage_page, new_unit_page, facility_manage_page, new_facility_page, delete_residence_page, delete_block_page,
    delete_unit_page, delete_facility_page, ResidenceViewSet, FacilityViewSet, UnitViewSet, FacilityUnitViewSet,
    BlockViewSet, UnitUserViewSet, BoardOfDirectorViewSet, FacilityResidenceViewSet,
    FacilityResidenceAccessibilityViewSet
)

app_name = 'building'

router = DefaultRouter()
router.register('residence', ResidenceViewSet, basename='residence')
router.register('facility', FacilityViewSet, basename='facility')
router.register('unit', UnitViewSet, basename='unit')
router.register('facility-unit', FacilityUnitViewSet, basename='facility-unit')
router.register('block', BlockViewSet, basename='block')
router.register('unit-user', UnitUserViewSet, basename='unit-user')
router.register('board-of-director', BoardOfDirectorViewSet, basename='board-of-director')
router.register('facility-residence', FacilityResidenceViewSet, basename='facility-residence')
router.register(
    'facility-residence-accessibility',
    FacilityResidenceAccessibilityViewSet,
    basename='facility-residence-accessibility'
)

urlpatterns = [
    #  Dashboard Paths =======================
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/residence/', residence_manage_page, name='residence_manage_page'),
    path('dashboard/residence/new/', new_residence_page, name='new_residence_page'),
    path('dashboard/residence/delete/', delete_residence_page, name='delete_residence_page'),
    # ####### Block Path ############
    path('dashboard/block/', block_manage_page, name='block_manage_page'),
    path('dashboard/block/new/', new_block_page, name='new_block_page'),
    path('dashboard/block/delete/', delete_block_page, name='delete_block_page'),

    # ####### Unit Path ############
    path('dashboard/unit/', unit_manage_page, name='unit_manage_page'),
    path('dashboard/unit/new/', new_unit_page, name='new_unit_page'),
    path('dashboard/unit/delete/', delete_unit_page, name='delete_unit_page'),

    # ####### Unit Path ############
    path('dashboard/facility/', facility_manage_page, name='facility_manage_page'),
    path('dashboard/facility/new/', new_facility_page, name='new_facility_page'),
    path('dashboard/facility/delete/', delete_facility_page, name='delete_facility_page'),

    # path('dashboard/facility/delete/', delete_facility_page, name='new_facility_page'),
    # path('dashboard/facility/edit/', edit_facility_page, name='new_facility_page'),
    path('api/', include(router.urls)),
]
