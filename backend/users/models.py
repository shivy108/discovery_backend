from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(unique=True)
    username = models.CharField(
        verbose_name='username',
        max_length=200,
        unique=True
    )
    first_name = models.CharField(
        verbose_name='first name',
        max_length=200,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name='last name',
        max_length=200,
        blank=True,
    )
    medical_id = models.CharField(
        verbose_name='medical ID',
        max_length=200,
        blank=True
    )
    is_staff = models.BooleanField(
        verbose_name='staff status',
        default=False,
        help_text='Designates whether the user can log into this site.',
    )
    is_active = models.BooleanField(
        verbose_name='active',
        default=True,
        help_text='Designates whether this user should be treated as active. '
                  'Unselect this instead of deleting accounts.'
    )
    date_joined = models.DateTimeField(
        verbose_name='date joined',
        auto_now_add=True
    )

    ########################
    # Social Profile
    avatar = models.ImageField(
        upload_to='',
        blank=True,
    )

    banner = models.ImageField(
        upload_to='',
        blank=True,
    )

    location = models.CharField(
        verbose_name='user location',
        max_length=200,
        blank=True
    )

    about_me = models.CharField(
        verbose_name='user description',
        max_length=1000,
        blank=True
    )

    medical_field = models.CharField(
        verbose_name='medical field',
        max_length=200,
        blank=True
    )

    def __str__(self):
        return self.username
