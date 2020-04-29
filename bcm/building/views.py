from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, mixins

# ###########Dashboard Base section #######################
from rest_framework.viewsets import GenericViewSet

from building.models import (
    Residence,
    Facility,
    Unit,
    FacilityUnit,
    Block,
    UnitUser,
    BoardOfDirector,
    FacilityResidence,
    FacilityResidenceAccessibility,
    UnitPhoneNumber,
    Budget,
    AccountingTarget,
)
from building.serializers import (
    ResidenceSerializer,
    FacilitySerializer,
    UnitSerializer,
    FacilityUnitSerializer,
    BlockSerializer,
    UnitUserSerializer,
    BoardOfDirectorSerializer,
    FacilityResidenceSerializer,
    FacilityResidenceAccessibilitySerializer,
    UnitPhoneNumberSerializer,
    BudgetSerializer,
    AccountingTargetListSerializer,
)
from users.models import User


def dashboard(request):
    # username = request.user.username
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
        'request_type': request_type,
        'users': User.objects.all(),
        'facilities': Facility.objects.all(),

    }
    return render(request, 'dashboard_pages/residence/new_residence.html', data)


def edit_residence_page(request, id):
    request_type = 'edit'
    data = {
        'residences': Residence.objects.all(),
        'residence': Residence.objects.filter(id=id).get(),
        # 'residence_manager': User.objects.filter(id=id).get(),
        'residence_facility': FacilityResidence.objects.filter(residence=id).all(),
        'facilities': Facility.objects.all(),
        'users': User.objects.all(),
        'request_type': request_type,
        'residence_id': id,
    }
    return render(request, 'dashboard_pages/residence/edit_residence.html', data)


def show_residence_page(request, id):
    request_type = 'show'
    data = {
        'residences': Residence.objects.all(),
        'residence': Residence.objects.filter(id=id).get(),
        'request_type': request_type,
        'id': id,
        'facilities': Facility.objects.all(),
        'residence_facility': FacilityResidence.objects.filter(residence=id).all(),
        'residence_id': id,

    }
    return render(request, 'dashboard_pages/residence/edit_residence.html', data)


# ##################### unit facility section  #######################


def unit_facility_manage_page(request, unit_id):
    response = {
        'data': FacilityUnit.objects.filter(unit=unit_id).all(),
        # 'residences': Block.objects.all(),
        'request_type': 'new',
        'unit_id': unit_id
    }
    return render(request, 'dashboard_pages/units/facility/unit_facility.html', response)


def new_unit_facility_page(request, unit_id):
    request_type = 'new'
    data = {
        'facilities': Facility.objects.all(),
        'unit_id': unit_id,
        'request_type': request_type,
    }
    return render(request, 'dashboard_pages/units/facility/new_unit_facility.html', data)


def edit_unit_facility_page(request, unit_id, id):
    request_type = 'edit'
    data = {
        'facilities': Facility.objects.all(),
        'unit_facility': FacilityUnit.objects.filter(id=id).get(),
        'request_type': request_type,
        'id': id,
        'unit_id': unit_id,
    }
    return render(request, 'dashboard_pages/units/facility/update_show_unit_facility.html', data)


def show_unit_facility_page(request, unit_id, id):
    request_type = 'show'
    data = {
        'facilities': Facility.objects.all(),
        'unit_facility': FacilityUnit.objects.filter(id=id).get(),
        'id': id,
        'request_type': request_type,
        'unit_id': unit_id,
    }
    return render(request, 'dashboard_pages/units/facility/update_show_unit_facility.html', data)


# ########################## unit phone numbers  ####################
def phone_number_manage_page(request, unit_id):
    response = {
        'data': UnitPhoneNumber.objects.filter(unit=unit_id).all(),
        # 'residences': Block.objects.all(),
        'request_type': 'new',
        'unit_id': unit_id
    }
    return render(request, 'dashboard_pages/units/phone_numbers/phone_number_managment.html', response)


def new_phone_number_page(request, unit_id):
    request_type = 'new'
    data = {
        # 'facilities': Facility.objects.all(),
        'unit_id': unit_id,
        'request_type': request_type,
    }
    return render(request, 'dashboard_pages/units/phone_numbers/new_phone_number.html', data)


def edit_phone_number_page(request, unit_id, id):
    request_type = 'edit'
    data = {
        'phone_number': UnitPhoneNumber.objects.filter(id=id).get(),
        'request_type': request_type,
        'id': id,
        'unit_id': unit_id,
    }
    return render(request, 'dashboard_pages/units/phone_numbers/update_show_phone_number.html', data)


def show_phone_number_page(request, unit_id, id):
    request_type = 'show'
    data = {
        'phone_number': UnitPhoneNumber.objects.filter(id=id).get(),
        'id': id,
        'request_type': request_type,
        'unit_id': unit_id,
    }
    return render(request, 'dashboard_pages/units/phone_numbers/update_show_phone_number.html', data)


# ########### Block section #######################


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


# ########### budget_manage_page  #############
def budget_manage_page(request):
    return render(request, 'dashboard_pages/budget/budget_management.html')


# ########### Income_manage_page  #############
def income_manage_page(request):
    request_type = 'new'

    data = {
        'request_type': request_type,
        'incomes': Budget.objects.filter(budget_class='INCOME').all()
    }
    return render(request, 'dashboard_pages/budget/income/income_management.html',data)


def new_income_page(request):
    request_type = 'new'
    data = {
        'residences': Residence.objects.all(),
        'blocks': Block.objects.all(),
        'units': Unit.objects.all(),
        'request_type': request_type
    }
    return render(request, 'dashboard_pages/budget/income/new_income.html', data)


def edit_income_page(request, id):
    request_type = 'edit'
    income = Budget.objects.filter(id=id).get()
    data = {
        'residences': Residence.objects.all(),
        'blocks': Block.objects.all(),
        'units': Unit.objects.all(),
        # 'residence': Residence.objects.filter(id=income.object_id),
        # 'block': Block.objects.filter(id=income.object_id),
        # 'unit': Unit.objects.filter(id=income.object_id),
        'income': income,
        'budget_targets': AccountingTarget.objects.filter(budgets=id).all(),
        # 'budget_targets' :
        'request_type': request_type,
        'id': id,
    # 'item_type_dropdown': item_type_dropdown
    }
    return render(request, 'dashboard_pages/budget/income/update_show_income.html',data)


def show_income_page(request,id):
    request_type = 'show'
    # item_type_dropdown = Residence.RESIDENCE_TYPE_CHOICES
    # data = {
    #     'facility': Facility.objects.filter(id=id).get(),
    #     'request_type': request_type,
    #     'id': id,
    # 'item_type_dropdown': item_type_dropdown
    # }
    return render(request, 'dashboard_pages/budget/income/update_show_income.html')


# ########### Expense_manage_page  #############
def expense_manage_page(request):
    request_type = 'new'

    data = {
        'request_type': request_type,
        'expenses': Budget.objects.filter(budget_class='EXPENSE').all()
    }
    return render(request, 'dashboard_pages/budget/expense/expense_management.html', data)


def new_expense_page(request):
    request_type = 'new'
    data = {
        'residences': Residence.objects.all(),
        'blocks': Block.objects.all(),
        'units': Unit.objects.all(),
        'request_type': request_type
    }
    return render(request, 'dashboard_pages/budget/expense/new_expense.html', data)


def edit_expense_page(request,id):
    request_type = 'edit'

    data = {
        'residences': Residence.objects.all(),
        'blocks': Block.objects.all(),
        'units': Unit.objects.all(),
        'expense': Budget.objects.filter(id=id).get(),
        'budget_targets': AccountingTarget.objects.filter(budgets=id).all(),
        # 'budget_targets' :
        'request_type': request_type,
        'id': id,
        # 'item_type_dropdown': item_type_dropdown
    }
    return render(request, 'dashboard_pages/budget/expense/update_show_expense.html', data)


def show_expense_page(request,id):
    # request_type = 'show'
    # item_type_dropdown = Residence.RESIDENCE_TYPE_CHOICES
    # data = {
    #     'facility': Facility.objects.filter(id=id).get(),
    #     'request_type': request_type,
    #     'id': id,
    # 'item_type_dropdown': item_type_dropdown
    # }
    return render(request, 'dashboard_pages/budget/expense/update_show_expense.html')

def bill_manage_page(request):
    response = {
        'users': User.objects.all(),
        # 'residences': Residence.objects.all(),
        'request_type': 'new'
    }
    return render(request, 'dashboard_pages/bill/bill_management.html', response)

def new_bill_page(request):
    request_type = 'new'
    data = {
        'users': User.objects.all(),
        'request_type': request_type
    }
    return render(request, 'dashboard_pages/bill/new_bill.html', data)


def edit_bill_page(request, id):
    request_type = 'edit'
    data = {
        'residences': Residence.objects.all(),
        'block_content': Block.objects.filter(id=id).get(),
        'request_type': request_type,
        'id': id,
        # 'item_type_dropdown': item_type_dropdown
    }
    return render(request, 'dashboard_pages/blocks/update_show_block.html', data)

def show_bill_page(request, id):
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


class UnitPhoneNumberViewSet(viewsets.ModelViewSet):
    queryset = UnitPhoneNumber.objects.all()
    serializer_class = UnitPhoneNumberSerializer


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


class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class AccountingTargetViewSet(mixins.CreateModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,
                              mixins.ListModelMixin,
                              GenericViewSet):
    queryset = AccountingTarget.objects.all()
    serializer_class = AccountingTargetListSerializer
