from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models

from django.utils.translation import ugettext_lazy as _
from lib.common_models import BaseModel
from location.models import Location

User = get_user_model()


class Post(BaseModel):
    caption = models.TextField(_('caption'), blank=True)
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return "{} {{}}".format(self.user.username, self.id)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")


class PostMedia(BaseModel):
    IMAGE = 1
    VIDEO = 2

    TYPE_CHOICES = (
        (IMAGE, _('Image')),
        (VIDEO, _('Video')),
    )
    media_types = models.PositiveSmallIntegerField(_('media types'), choices=TYPE_CHOICES, default=IMAGE)
    post = models.ForeignKey(Post, related_name="media", on_delete=models.CASCADE)
    media_file = models.FileField(_('media files'), upload_to='content/media/',
                                  validators=[FileExtensionValidator(allowed_extensions=('jpg', 'jpeg', 'mpd'))])

    def __str__(self):
        return '{} >> {}'.format(str(self.post), self.get_media_type_display())

    class Meta:
        verbose_name = _("PostMedia")
        verbose_name_plural = _("PostMedias")


class Tag(BaseModel):
    title = models.CharField(_('title'), max_length=32)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _("Tags")


class PostTag(BaseModel):
    post = models.ForeignKey(Post, related_name='hashtags', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("PostTag")
        verbose_name_plural = _("PostTags")


class TagegedUser(BaseModel):
    user = models.ForeignKey(User, related_name='tagged_posts', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='tagged_post', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("TaggedUser")
        verbose_name_plural = _("TaggedUsers")
