from time import sleep

from celery import shared_task
from celery.schedules import crontab
from celery.task import task, periodic_task
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


@task(name='Send phone verification code')
def send_phone_verification_code(username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return None
    sleep(10)
    return "verification code sent to user: {}".format(username)


@shared_task(name='Send email verification link')
def send_email_verification_link(username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return None
    # Send email
    sleep(10)
    return "Link sent to user: {}".format(username)


@periodic_task(name='Time pinger', run_every=crontab(minute='*'))
def minute_pinger():
    return 'time: {}'.format(timezone.now())


@periodic_task(name='Time 3 minute pinger', run_every=crontab(minute='*/3'))
def minute_three_pinger():
    return 'time: {}'.format(timezone.now())


@periodic_task(name='Notify unverified users', run_every=crontab(day_of_month='1'))
def check_unverified_users():
    for user in User.objects.all():
        # if user is not verified
        send_email_verification_link.delay(user.username)
        send_phone_verification_code.delay(user.username)
