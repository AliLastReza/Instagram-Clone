from django.contrib.auth import get_user_model
from django.db import models

from lib.common_models import BaseModel

User = get_user_model()


class Relation(BaseModel):
    from_user = models.ForeignKey(User, related_name='followings', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

    def _str__(self):
        return "{} >> {}".format(self.from_user.username, self.to_user.username)
