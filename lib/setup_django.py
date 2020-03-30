import django

from django.conf import settings

from instagram.settings import DATABASES, INSTALLED_APPS


def setup_django():
    settings.configure(DATABASES=DATABASES, INSTALLED_APPS=INSTALLED_APPS)
    django.setup()
