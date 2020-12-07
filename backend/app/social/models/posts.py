from django.conf import settings
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    content = models.TextField(
        verbose_name='content'
    )
    created = models.DateTimeField(
        verbose_name='created',
        auto_now_add=True,
    )

    shared = models.ForeignKey(
        verbose_name='shared post',
        to='self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='sharing_posts'
    )

    def __str__(self):
        return f"{self.user}: {self.content[:50]} ..."
