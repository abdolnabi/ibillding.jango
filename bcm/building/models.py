from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from django_mysql.models import EnumField, JSONField

from building.enums import (
    ResidenceType,
    FacilityType,
    UnitUserType,
    FacilityResidenceAccessibilitiesType,
    BillClassType,
    BillType,
    BillCurrency,
    BillStatus,
    AdvertisementType,
    AdvertisementStatus,
    PaymentStatus,
    BudgetClassType,
)
from core.models import BaseModel
from users.models import User


class Location(models.Model):
    latitude = models.FloatField(
        verbose_name=_('latitude'),
        help_text=_('latitude for this location'),
        blank=True,
        null=True,
    )
    longitude = models.FloatField(
        verbose_name=_('longitude'),
        help_text=_('longitude for this location'),
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.latitude}-{self.longitude}'


class Residence(BaseModel):
    RESIDENCE_TYPE_CHOICES = (
        (ResidenceType.BUILDING, _('Building')),
        (ResidenceType.COMPLEX, _('Complex')),
        (ResidenceType.LOCAL_SHOP, _('Local shop')),
        (ResidenceType.TOWN, _('Town')),
    )

    parent_residence = models.ForeignKey(
        verbose_name=_('parent residence'),
        help_text=_('parent residence for this residence'),
        to='self',
        on_delete=models.PROTECT,
        related_name='residence_parent',
        blank=True,
        null=True,
    )

    manager = models.ForeignKey(
        verbose_name=_('manager'),
        help_text=_('manager for this residence'),
        to=User,
        on_delete=models.PROTECT,
        related_name='managers'
    )

    name = models.CharField(
        verbose_name=_('name'),
        help_text=_('residence name'),
        max_length=255
    )

    type = EnumField(
        verbose_name=_('type'),
        help_text=_('type of this residence'),
        choices=RESIDENCE_TYPE_CHOICES,
        default=ResidenceType.BUILDING,
    )

    address = models.TextField(
        verbose_name=_('Address'),
        help_text=_('Address of residence'),
    )

    coordinate = models.ForeignKey(
        verbose_name=_('coordinate'),
        help_text=_('coordinate for this residence'),
        to=Location,
        on_delete=models.CASCADE,
        related_name='coordinates'
    )

    rules = models.TextField(
        verbose_name=_('rules'),
        help_text=_('rules for this residence'),
    )

    appendix_to_statute = models.TextField(
        verbose_name=_('appendix to statute'),
        help_text=_('appendix to statute for this residence'),
    )

    users_board = models.ManyToManyField(
        verbose_name=_('users board'),
        help_text=_('users board'),
        to=User,
        through='BoardOfDirector',
    )

    accounting_targets = GenericRelation('AccountingTarget')

    def __str__(self):
        return self.name


class Facility(BaseModel):
    FACILITIES_TYPE_CHOICES = (
        (FacilityType.RESIDENCE, _('Residence')),
        (FacilityType.ALL, _('All')),
        (FacilityType.BLOCK, _('Block')),
        (FacilityType.UNIT, _('Unit')),
    )

    title = models.CharField(
        verbose_name=_('title'),
        help_text=_('title for this facility'),
        max_length=255
    )

    description = models.TextField(
        verbose_name=_('description'),
        help_text=_('description for this facility'),
    )

    type = EnumField(
        verbose_name=_('Type'),
        help_text=_('type of Facility'),
        choices=FACILITIES_TYPE_CHOICES,
        default=FacilityType.BLOCK,
    )

    units = models.ManyToManyField(
        verbose_name=_('Units'),
        help_text=_('Units for this Facility'),
        to='Unit',
        through='FacilityUnit',
    )

    def __str__(self):
        return self.title


class Unit(BaseModel):
    residence = models.ForeignKey(
        verbose_name=_('residence'),
        help_text=_('residence of this unit'),
        to=Residence,
        on_delete=models.CASCADE,
    )

    area = models.DecimalField(
        verbose_name=_('area'),
        help_text=_('area for this unit'),
        max_digits=6,
        decimal_places=2,
    )

    population = models.PositiveIntegerField(
        verbose_name=_('population'),
        help_text=_('population of this unit')
    )

    # def __str__(self):
    #     return self.residence

    users = models.ManyToManyField(
        verbose_name=_('users'),
        help_text=_('users for Unit'),
        to=User,
        through='UnitUser',
    )

    accounting_targets = GenericRelation('AccountingTarget')


class FacilityUnit(BaseModel):
    unit = models.ForeignKey(
        verbose_name=_('unit'),
        help_text=_('unit for this facility unit'),
        to=Unit,
        on_delete=models.CASCADE,
        related_name='Facilities'
    )

    facility = models.ForeignKey(
        verbose_name=_('facility'),
        help_text=_('facility for this facility unit'),
        to=Facility,
        on_delete=models.CASCADE
    )

    second_title = models.CharField(
        verbose_name=_('second title'),
        help_text=_('second title for this facility unit'),
        max_length=255
    )

    description = models.TextField(
        verbose_name=_('description'),
        help_text=_('description for this facility unit')
    )


class Block(BaseModel):
    residence = models.ForeignKey(
        verbose_name=_('residence'),
        help_text=_('residence for this block'),
        to=Residence,
        on_delete=models.PROTECT,
    )

    name = models.CharField(
        verbose_name=_('name'),
        help_text=_('name of block'),
        max_length=255
    )

    number_of_floors = models.PositiveIntegerField(
        verbose_name=_('number of floors'),
        help_text=_('number of block floors')
    )

    number_of_units = models.PositiveIntegerField(
        verbose_name=_('number of Units'),
        help_text=_('number of block Units'),
    )

    accounting_targets = GenericRelation('AccountingTarget')

    def __str__(self):
        return self.name


class UnitUser(BaseModel):
    UNIT_USER_TYPE_CHOICES = (
        (UnitUserType.RESIDENT, _('Resident')),
        (UnitUserType.BOTH, _('Both')),
        (UnitUserType.OWNER, _('Owner'))
    )

    user = models.ForeignKey(
        verbose_name=_('user'),
        help_text=_('user for this user unit'),
        to=User,
        on_delete=models.CASCADE,
        related_name='Units',
    )

    unit = models.ForeignKey(
        verbose_name=_('unit'),
        help_text=_('unit for this user unit'),
        to=Unit,
        on_delete=models.CASCADE,
    )

    type = EnumField(
        verbose_name=_('type'),
        help_text=_('type of user'),
        choices=UNIT_USER_TYPE_CHOICES,
        default=UnitUserType.RESIDENT,
    )

    confirmed = models.BooleanField(
        verbose_name=_('confirmed'),
        help_text=_('confirmation for user'),
        default=True,
    )


class BoardOfDirector(BaseModel):
    residence = models.ForeignKey(
        verbose_name=_('residence'),
        help_text=_('residence of board'),
        to=Residence,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        verbose_name=_('user'),
        help_text=_('user of board'),
        to=User,
        on_delete=models.CASCADE,
        related_name='residence_board'
    )

    role = models.CharField(
        verbose_name=_('role'),
        help_text=_('role of board'),
        max_length=255,
    )


class FacilityResidence(BaseModel):
    residence = models.ForeignKey(
        verbose_name=_('residence'),
        help_text=_('residence for this facility residence'),
        to=Residence,
        on_delete=models.CASCADE,
        related_name='facility_residences'
    )

    facility = models.ForeignKey(
        verbose_name=_('facility'),
        help_text=_('facility for this facility residence'),
        to=Facility,
        on_delete=models.CASCADE,
    )

    second_title = models.CharField(
        verbose_name=_('second title'),
        help_text=_('second title for this facility residence'),
        max_length=255,
    )

    description = models.TextField(
        verbose_name=_('description'),
        help_text=_('description for this facility residence'),
    )

    requestable = models.BooleanField(
        verbose_name=_('requestable'),
        help_text=_('requestable for this facility residence'),
        default=False,
    )

    price = models.DecimalField(
        verbose_name=_('price'),
        help_text=_('price for this facility residence'),
        max_digits=10,
        decimal_places=2,
    )

    blocks = models.ManyToManyField(
        verbose_name=_('blocks'),
        help_text=_('blocks for this this facility residence'),
        to=Block,
        related_name='facility_residence',
        blank=True,
    )


class FacilityResidenceAccessibility(BaseModel):
    FACILITY_RESIDENCE_ACCESSIBILITY_CHOICES = (
        (FacilityResidenceAccessibilitiesType.PUBLIC, _('Public')),
        (FacilityResidenceAccessibilitiesType.BLOCK, _('Block')),
        (FacilityResidenceAccessibilitiesType.UNIT, _('Unit')),
        (FacilityResidenceAccessibilitiesType.RESIDENCE, _('Residence')),
    )

    facility_residence = models.ForeignKey(
        verbose_name=_('facility residence'),
        help_text=_('facility residence for this object'),
        to=FacilityResidence,
        on_delete=models.CASCADE,
    )

    type = EnumField(
        verbose_name=_('type'),
        help_text=_('choose type for this accessibility'),
        choices=FACILITY_RESIDENCE_ACCESSIBILITY_CHOICES,
    )

    accessible = models.BigIntegerField(
        verbose_name=_('accessible'),
        help_text=_('accessible for this accessibility'),
    )


class UnitPhoneNumber(BaseModel):
    unit = models.ForeignKey(
        verbose_name=_('unit'),
        help_text=_('unit for this phone'),
        to=Unit,
        on_delete=models.CASCADE,
        related_name='phone_numbers'
    )

    phone = models.CharField(
        verbose_name=_('phone'),
        help_text=_('the phone number'),
        max_length=16,
    )

    description = models.TextField(
        verbose_name=_('description'),
        help_text=_('description'),
        blank=True,
    )

    def __str__(self):
        return self.phone


class Budget(BaseModel):
    BUDGET_CLASS_CHOICES = (
        (BudgetClassType.EXPENSE, _('Expense')),
        (BudgetClassType.INCOME, _('Income'))
    )

    title = models.CharField(
        verbose_name=_('title'),
        help_text=_('title for budget'),
        max_length=64,
    )

    budget_class = EnumField(
        verbose_name=_('class'),
        help_text=_('budget class'),
        choices=BUDGET_CLASS_CHOICES,
        default=BudgetClassType.EXPENSE,
    )

    period = models.IntegerField(
        verbose_name=_('period'),
        help_text=_('period of budget'),
        default=0,
    )

    start_at = models.DateTimeField(
        verbose_name=_('start at'),
        help_text=_('start at this time'),
    )

    deadline_in_days = models.IntegerField(
        verbose_name=_('deadline in days'),
        help_text=_('deadline in days'),
        blank=True,
        null=True,
    )

    finish_at = models.DateTimeField(
        verbose_name=_('finish at'),
        help_text=_('finish at this time'),
    )

    due_at = models.DateTimeField(
        verbose_name=_('due at'),
        help_text=_('due at this time'),
    )

    price = models.DecimalField(
        verbose_name=_('price'),
        help_text=_('price of budget'),
        max_digits=10,
        decimal_places=2,
    )

    price_formula = models.TextField(
        verbose_name=_('price formula'),
        help_text=_('price formula'),
    )

    parameters = JSONField(
        verbose_name=_('parameters'),
        help_text=_('parameters of formula'),
    )

    def __str__(self):
        return self.title


class Bill(BaseModel):
    BILL_CLASS_CHOICES = (
        (BillClassType.EXPENSE, _('Expense')),
        (BillClassType.INCOME, _('Income')),
    )
    BILL_TYPE_CHOICES = (
        (BillType.ADVERTISEMENT, _('Advertisement')),
        (BillType.BUDGET, _('Budget')),
        (BillType.REQUEST, _('Request')),
        (BillType.SETTLEMENT_REQUEST, _('Settlement request')),
    )

    BILL_CURRENCY_CHOICES = (
        (BillCurrency.IRR, _('IRR')),
        (BillCurrency.USD, _('USD')),
    )

    BILL_STATUS_CHOICES = (
        (BillStatus.CONFIRMED, _('Confirmed')),
        (BillStatus.EXPIRED, _('Expired')),
        (BillStatus.PENDING, _('Pending')),
        (BillStatus.REJECTED, _('Rejected')),
    )

    user = models.ForeignKey(
        verbose_name=_('user'),
        help_text=_('owner of bill'),
        to=User,
        on_delete=models.CASCADE,
        related_name='bills'
    )

    bill_class = EnumField(
        verbose_name=_('class'),
        help_text=_('class'),
        choices=BILL_CLASS_CHOICES,
        default=BillClassType.EXPENSE,
    )

    type = EnumField(
        verbose_name=_('type'),
        help_text=_('type of bill'),
        choices=BILL_TYPE_CHOICES,
        default=BillType.BUDGET,
    )

    due_at = models.DateTimeField(
        verbose_name=_('due at'),
        help_text=_('due at'),
    )

    price = models.DecimalField(
        verbose_name=_('price'),
        help_text=_('bill price'),
        max_digits=10,
        decimal_places=2,
    )

    currency = EnumField(
        verbose_name=_('currency'),
        help_text=_('bill currency'),
        choices=BILL_CURRENCY_CHOICES,
        default=BillCurrency.IRR
    )

    description = models.TextField(
        verbose_name=_('description'),
        help_text=_('description of bill'),
    )

    status_description = models.TextField(
        verbose_name=_('status description'),
        help_text=_('status description'),
    )

    status = EnumField(
        verbose_name=_('status'),
        help_text=_('status of bill'),
        choices=BILL_STATUS_CHOICES,
        default=BillStatus.PENDING,
    )


class Advertisement(BaseModel):
    ADVERTISEMENT_TYPE_CHOICES = (
        (AdvertisementType.GLOBAL, _('Global')),
        (AdvertisementType.LOCAL, _('local')),
    )

    ADVERTISEMENT_STATUS_CHOICES = (
        (AdvertisementStatus.ACTIVE, _('Active')),
        (AdvertisementStatus.INACTIVE, _('Inactive')),
    )

    type = EnumField(
        verbose_name=_('type'),
        help_text=_('type of advertisement'),
        choices=ADVERTISEMENT_TYPE_CHOICES,
        default=AdvertisementType.LOCAL,
    )

    content = models.TextField(
        verbose_name=_('content'),
        help_text=_('content of advertisement'),
    )

    bill = models.ForeignKey(
        verbose_name=_('bill'),
        help_text=_('bill of advertisement'),
        to=Bill,
        on_delete=models.CASCADE,
        related_name='advertisements'
    )

    status = EnumField(
        verbose_name=_('status'),
        help_text=_('status of advertisement'),
        choices=ADVERTISEMENT_STATUS_CHOICES,
        default=AdvertisementStatus.INACTIVE,
    )

    description = models.TextField(
        verbose_name=_('text'),
        help_text=_('text of advertisement'),
    )


class PaymentGateway(BaseModel):
    name = models.CharField(
        verbose_name=_('name'),
        help_text=_('name of payment gateway'),
        max_length=255
    )

    credentials = JSONField(
        verbose_name=_('credentials'),
        help_text=_('credentials')
    )


class Payment(BaseModel):
    PAYMENT_STATUS_CHOICES = (
        (PaymentStatus.PENDING, _('Pending')),
        (PaymentStatus.REJECTED, _('Rejected')),
        (PaymentStatus.EXPIRED, _('Expired')),
        (PaymentStatus.CONFIRMED, _('Confirmed')),
    )
    bill = models.ForeignKey(
        verbose_name=_('bill'),
        help_text=_('bill'),
        to=Bill,
        on_delete=models.CASCADE,
        related_name='payments'
    )

    payment_gateway = models.ForeignKey(
        verbose_name=_('payment gateway'),
        help_text=_('payment gateway'),
        to=PaymentGateway,
        on_delete=models.CASCADE,
        related_name='payments'
    )

    payer = models.ForeignKey(
        verbose_name=_('payer'),
        help_text=_('payer'),
        to=User,
        on_delete=models.CASCADE,
        related_name='payments'
    )

    info = JSONField(
        verbose_name=_('info'),
        help_text=_('info'),
    )

    status = EnumField(
        verbose_name=_('status'),
        help_text=_('status of payment'),
        choices=PAYMENT_STATUS_CHOICES,
        default=PaymentStatus.PENDING
    )


class AccountingTarget(BaseModel):
    app_label = 'building'
    accounting_target_limit = (
            Q(app_label=app_label, model='residence') |
            Q(app_label=app_label, model='block') |
            Q(app_label=app_label, model='unit')
    )
    accounting_target_choice = (
       (ContentType.objects.get(model='residence').id, _('residence')),
       (ContentType.objects.get(model='block').id, _('block')),
       (ContentType.objects.get(model='unit').id, _('unit')),
    )

    content_type = models.ForeignKey(
        verbose_name=_('content type'),
        help_text=_('content type'),
        to=ContentType,
        on_delete=models.CASCADE,
        limit_choices_to=accounting_target_limit,
        choices=accounting_target_choice,
        default=accounting_target_choice[0][0]
    )

    object_id = models.PositiveIntegerField(
        verbose_name=_('object id'),
        help_text=_('object id'),
    )

    content_object = GenericForeignKey('content_type', 'object_id')

    budgets = models.ManyToManyField(
        verbose_name=_('budgets'),
        help_text=_('budgets'),
        to='Budget',
        related_name='accounting_targets',
        null=True,
        blank=True,
    )

    bills = models.ManyToManyField(
        verbose_name=_('bills'),
        help_text=_('bills'),
        to='Bill',
        related_name='accounting_targets',
        null=True,
        blank=True,
    )
