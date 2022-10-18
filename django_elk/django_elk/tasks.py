from celery import shared_task
from django.core.management import call_command
from io import StringIO

@shared_task
def test_elk_connection():
    call_command('test_connection')

@shared_task
def echo_message():
    out = StringIO()
    call_command('echo_message', stdout=out)
    return out.getvalue()

