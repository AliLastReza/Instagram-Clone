from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

from activity.models import Comment
from content.models import Post

User = get_user_model()


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        count = options['count']
        user = User.objects.first()
        if user is None:
            User.objects.create_user(username='test1', email='test@mail.com', password='12345678')
        post = Post.objects.filter(user=user).first()
        if post is None:
            post = Post.objects.create(user=user, caption="Test for load comments")
        for _ in range(count):
            Comment.objects.create(caption="Test command Comment", user=user, post=post)

