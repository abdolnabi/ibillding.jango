# from django.contrib.gis.db import models as gis_models
from django.db import models
from django.utils.translation import ugettext_lazy as _

from building.enums import ResidencesType, FacilitiesType, UnitUserType, FacilityResidenceAccessibilitiesType
from core.models import BaseModel
from users.models import User


class Residences(BaseModel):
    RESIDENCES_TYPE_CHOICES = (
        (ResidencesType.BUILDING, _('Building')),
        (ResidencesType.COMPLEX, _('Complex')),
        (ResidencesType.LOCAL_SHOP, _('Local shop')),
        (ResidencesType.TOWN, _('Town')),
    )

    parent_residences = models.ForeignKey(
        verbose_name=_('parent residences'),
        help_text=_('parent residences for this residences'),
        to='self',
        on_delete=models.PROTECT,
        related_name='residences_parent',
        blank=True,
        null=True,
    )

    manager = models.ForeignKey(
        verbose_name=_('manager'),
        help_text=_('manager for this residences'),
        to=User,
        on_delete=models.PROTECT,
        related_name='managers'
    )

    name = models.CharField(
        verbose_name=_('name'),
        help_text=_('residences name'),
        max_length=255
    )

    type = models.CharField(
        verbose_name=_('type'),
        help_text=_('type of this residences'),
        max_length=32,
        choices=RESIDENCES_TYPE_CHOICES,
        default=ResidencesType.BUILDING,
    )

    address = models.TextField(
        verbose_name=_('Address'),
        help_text=_('Address of residences'),
    )

    # coordinate = gis_models.PointField(
    #     verbose_name=_('coordinate'),
    #     help_text=_('coordinate for this residences'),
    # )

    rules = models.TextField(
        verbose_name=_('rules'),
        help_text=_('rules for this residences'),
    )

    appendix_to_statute = models.TextField(
        verbose_name=_('appendix to statute'),
        help_text=_('appendix to statute for this residences'),
    )

    users_board = models.ManyToManyField(
        verbose_name=_('users board'),
        help_text=_('users board'),
        to=User,
        through='BoardOfDirectors',
    )

    def __str__(self):
        return self.name


class Facilities(BaseModel):
    FACILITIES_TYPE_CHOICES = (
        (FacilitiesType.RESIDENCE, _('Residence')),
        (FacilitiesType.ALL, _('All')),
        (FacilitiesType.BLOCK, _('Block')),
        (FacilitiesType.UNIT, _('Unit')),
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

    type = models.CharField(
        verbose_name=_('Type'),
        help_text=_('type of Facilities'),
        max_length=32,
        choices=FACILITIES_TYPE_CHOICES,
        default=FacilitiesType.BLOCK,
    )

    units = models.ManyToManyField(
        verbose_name=_('Units'),
        help_text=_('Units for this Facilities'),
        to='Unit',
        through='FacilityUnit',
    )

    def __str__(self):
        return self.title


class Unit(BaseModel):
    residences = models.ForeignKey(
        verbose_name=_('residences'),
        help_text=_('residences of this unit'),
        to=Residences,
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
    #     return self.residences

    users = models.ManyToManyField(
        verbose_name=_('users'),
        help_text=_('users for Units'),
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
        to=Facilities,
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
        verbose_name=_('residences'),
        help_text=_('residence for this block'),
        to=Residences,
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

    type = models.CharField(
        verbose_name=_('type'),
        help_text=_('type of user'),
        choices=UNIT_USER_TYPE_CHOICES,
        default=UnitUserType.RESIDENT,
        max_length=32,
    )

    confirmed = models.BooleanField(
        verbose_name=_('confirmed'),
        help_text=_('confirmation for user'),
        default=True,
    )


class BoardOfDirectors(BaseModel):
    residence = models.ForeignKey(
        verbose_name=_('residence'),
        help_text=_('residence of board'),
        to=Residences,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        verbose_name=_('user'),
        help_text=_('user of board'),
        to=User,
        on_delete=models.CASCADE,
        related_name='residences_board'
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
        to=Residences,
        on_delete=models.CASCADE,
    )

    facility = models.ForeignKey(
        verbose_name=_('facility'),
        help_text=_('facility for this facility residence'),
        to=Facilities,
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
        related_name='facility_residences',
    )


class FacilityResidenceAccessabilities(BaseModel):
    FACILITY_RESIDENCE_ACCESSIBLILITY_CHOICES = (
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

    type = models.CharField(
        verbose_name=_('type'),
        help_text=_('choose type for this accessibility'),
        choices=FACILITY_RESIDENCE_ACCESSIBLILITY_CHOICES,
        max_length=32,
    )

    accessible = models.BigIntegerField(
        verbose_name=_('accessible'),
        help_text=_('accessible for this accessibility'),
    )
