from django.conf import settings
from random import randint
from django.db import models


def code_generator():
    return str(randint(100000, 999999))


class RegistrationProfile(models.Model):
    user = models.OneToOneField(
        verbose_name='user',
        on_delete=models.CASCADE,
        related_name='registration_profile',
        to=settings.AUTH_USER_MODEL
    )
    code = models.CharField(
        verbose_name='code',
        help_text='code used for Registration and for password reset',
        max_length=6,
        default=code_generator
    )
    code_type = models.CharField(
        verbose_name='code type',
        max_length=2,
        choices=(
            ('RV', 'Registration Validation'),
            ('PR', 'Password Reset')
        )
    )
    code_used = models.BooleanField(
        verbose_name='code used',
        default=False
    )

    def __str__(self):
        return f'{self.user.email}, {self.code}'
