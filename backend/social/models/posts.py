from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(
        verbose_name="user",
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name="posts",
    )
    content = models.TextField(verbose_name="content")
    medical_field = models.CharField(
        verbose_name="medical field", max_length=200, null=True)
    created = models.DateTimeField(verbose_name="created", auto_now_add=True,)
