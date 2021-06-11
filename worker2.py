"""Implements celery worker (task consumer)."""

from time import sleep

from celery_app import celery_app2, logger


@celery_app2.task
def sub(x, y):
    result = x - y
    logger.info(f"{x} - {y} = {result}")
    sleep(35)
    return result
