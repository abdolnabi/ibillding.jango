from django.urls import path, include
from rest_framework.routers import DefaultRouter

from building.views import (
    dashboard,
    residence_manage_page,
    new_residence_page,
    new_block_page,
    block_manage_page,
    unit_manage_page,
    new_unit_page,
    facility_manage_page,
    new_facility_page,
    ResidenceViewSet,
    FacilityViewSet,
    UnitViewSet,
    FacilityUnitViewSet,
    BlockViewSet,
    UnitUserViewSet,
    BoardOfDirectorViewSet,
    FacilityResidenceViewSet,
    FacilityResidenceAccessibilityViewSet,
    edit_residence_page,
    show_residence_page,
    show_block_page,
    edit_block_page,
    edit_unit_page,
    show_unit_page,
    edit_facility_page,
    show_facility_page,
    show_unit_facility_page,
    new_unit_facility_page,
    unit_facility_manage_page,
    edit_unit_facility_page,
    phone_number_manage_page,
    new_phone_number_page,
    show_phone_number_page,
    edit_phone_number_page,
    UnitPhoneNumberViewSet,
    BudgetViewSet,
    budget_manage_page,
    income_manage_page,
    new_income_page,
    edit_income_page,
    show_income_page,
    expense_manage_page,
    new_expense_page,
    edit_expense_page,
    show_expense_page,
    bill_manage_page,
    edit_bill_page,
    new_bill_page,
    show_bill_page,
    AccountingTargetViewSet,
    BillViewSet,
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
router.register('phone-number', UnitPhoneNumberViewSet, basename='phone-number')
router.register('budget', BudgetViewSet, basename='budget')
router.register('bill', BillViewSet, basename='bill')
router.register('accounting-target', AccountingTargetViewSet, basename='accounting-target')

urlpatterns = [
    #  Dashboard Paths =======================
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/residence/', residence_manage_page, name='residence_manage_page'),
    path('dashboard/residence/new/', new_residence_page, name='new_residence_page'),
    path('dashboard/residence/edit/<int:id>', edit_residence_page, name='edit_residence_page'),
    path('dashboard/residence/show/<int:id>', show_residence_page, name='show_residence_page'),
    # path('dashboard/residence/<int:id>', residence_page, name='residence_page'),
    # ####### Block Path ############
    path('dashboard/block/', block_manage_page, name='block_manage_page'),
    path('dashboard/block/new/', new_block_page, name='new_block_page'),
    path('dashboard/block/edit/<int:id>', edit_block_page, name='edit_block_page'),
    path('dashboard/block/show/<int:id>', show_block_page, name='show_block_page'),

    # ####### Unit Path ############
    path('dashboard/unit/', unit_manage_page, name='unit_manage_page'),
    path('dashboard/unit/new/', new_unit_page, name='new_unit_page'),
    path('dashboard/unit/edit/<int:id>', edit_unit_page, name='edit_unit_page'),
    path('dashboard/unit/show/<int:id>', show_unit_page, name='show_unit_page'),
    # ####### Unit Facility Path ############
    path('dashboard/unit/<int:unit_id>/facility', unit_facility_manage_page, name='unit_facility_manage_page'),
    path('dashboard/unit/<int:unit_id>/edit_facility/<int:id>', edit_unit_facility_page,
         name='edit_unit_facility_page'),
    path('dashboard/unit/<int:unit_id>/facility/<int:id>', show_unit_facility_page, name='show_unit_facility_page'),
    path('dashboard/unit/<int:unit_id>/facility/new/', new_unit_facility_page, name='new_unit_facility_page'),
    # ####### Unit phone numbers Path ############
    path('dashboard/unit/<int:unit_id>/phone_number', phone_number_manage_page, name='phone_number_manage_page'),
    path('dashboard/unit/<int:unit_id>/edit_phone_number/<int:id>', edit_phone_number_page,
         name='edit_phone_number_page'),
    path('dashboard/unit/<int:unit_id>/phone_number/<int:id>', show_phone_number_page, name='show_phone_number_page'),
    path('dashboard/unit/<int:unit_id>/phone_number/new/', new_phone_number_page, name='new_phone_number_page'),

    # ####### facility Path ############
    path('dashboard/facility/', facility_manage_page, name='facility_manage_page'),
    path('dashboard/facility/new/', new_facility_page, name='new_facility_page'),
    path('dashboard/facility/edit/<int:id>', edit_facility_page, name='edit_facility_page'),
    path('dashboard/facility/show/<int:id>', show_facility_page, name='show_facility_page'),

    # ############# budget section  #############
    path('dashboard/budget', budget_manage_page, name='budget_manage_page'),
    # ############# budget- income section  #############
    path('dashboard/income', income_manage_page, name='income_manage_page'),
    path('dashboard/income/new/', new_income_page, name='new_income_page'),
    path('dashboard/income/edit/<int:id>', edit_income_page, name='edit_income_page'),
    path('dashboard/income/show/<int:id>', show_income_page, name='show_income_page'),
    # ############# budget- income section  #############
    path('dashboard/expense', expense_manage_page, name='expense_manage_page'),
    path('dashboard/expense/new/', new_expense_page, name='new_expense_page'),
    path('dashboard/expense/edit/<int:id>', edit_expense_page, name='edit_expense_page'),
    path('dashboard/expense/show/<int:id>', show_expense_page, name='show_expense_page'),

    # ####### bill Path ############
    path('dashboard/bill/', bill_manage_page, name='bill_manage_page'),
    path('dashboard/bill/new/', new_bill_page, name='new_bill_page'),
    path('dashboard/bill/edit/<int:id>', edit_bill_page, name='edit_bill_page'),
    path('dashboard/bill/show/<int:id>', show_bill_page, name='show_bill_page'),

    path('api/', include(router.urls)),
]
