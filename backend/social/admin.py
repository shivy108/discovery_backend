from django.contrib import admin

from social.models.posts import Post
from social.models.friends import Friend
from social.models.comments import Comment

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Friend)
