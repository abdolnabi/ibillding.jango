from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import BaseModel
from users.managers import UserManager


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name=_('username'),
        help_text=_('username for this user'),
        unique=True,
        max_length=128,
    )

    first_name = models.CharField(
        verbose_name=_('first name'),
        help_text=_('first name for this user'),
        max_length=255,
    )

    last_name = models.CharField(
        verbose_name=_('last name'),
        help_text=_('last name for this user'),
        max_length=255,

    )

    email = models.EmailField(
        verbose_name=_('email'),
        help_text=_('email for this user'),
        blank=True,
    )

    iban = models.CharField(
        verbose_name=_('iban'),
        help_text=_('iban for this user'),
        max_length=128,
    )

    financial_credit = models.DecimalField(
        verbose_name=_('financial credit'),
        help_text=_('financial credit for this user'),
        max_digits=10,
        decimal_places=2,
    )

    is_admin = models.BooleanField(
        verbose_name=_('is admin'),
        help_text=_('is this user admin?'),
        default=False,
    )

    is_active = models.BooleanField(
        verbose_name=_('is active'),
        help_text=_('is this user active?'),
        default=True,
    )

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'email')

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username

    def set_role(self, role):
        self.role = role
        self.save()

    @property
    def full_name(self):
        if not self.first_name and not self.last_name:
            return self.username

        if not self.last_name:
            return self.first_name

        return f"{self.first_name} {self.last_name}"

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        return self.is_admin
