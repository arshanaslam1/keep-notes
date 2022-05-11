
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username_alphanumeric_validator = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Only alphanumeric characters are allowed'),
        validators=[username_alphanumeric_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        }
    )
    first_name = models.CharField(_('first name'), max_length=150, blank=True, null=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=True, null=False)
    date_of_birth = models.DateField(_('date_of_birth'), max_length=150, blank=True, null=True)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to="profiles/avatars/", default='default.png', null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.id})
