from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_mysql.models import EnumField

from building.enums import ResidenceType, FacilityType, UnitUserType, FacilityResidenceAccessibilitiesType
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
