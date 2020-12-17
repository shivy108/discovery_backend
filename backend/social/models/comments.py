from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

from social.models.posts import Post

User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
        null=True
    )

    post = models.ForeignKey(
        verbose_name='post',
        to=Post,
        related_name='comments',
        on_delete=models.CASCADE,
        null=True
    )

    comment = models.CharField(
        verbose_name='comment',
        max_length=1000,
        null=True
    )

    created = models.DateTimeField(
        verbose_name='created time',
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.user} post a comment: {self.comment[:20]}..."
