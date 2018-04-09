from __future__ import absolute_import, unicode_literals
import logging

from django.conf import settings
from aslm.celery import app

logger = logging.getLogger("celery")


@app.task
def show_hello_world(user):
    logger.info("Printing Hello from Celery")
    logger.info("Second Printing Hello from Celery")
