from django.contrib.auth import get_user_model
from django.db import models

from content.models import Post
from lib.common_models import BaseModel
from django.utils.translation import ugettext_lazy as _

USER = get_user_model()


class Comment(BaseModel):
    caption = models.TextField()
    user = models.ForeignKey(USER, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    replay_to = models.ForeignKey('self', related_name='replays', on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

class Like(BaseModel):
    user = models.ForeignKey(USER, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post , related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
        return '{} >> {}'.format(self.user.username, self.post)

    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")