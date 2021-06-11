"""Implements celery worker (task consumer)."""

from celery_app import celery_app2, logger


@celery_app2.task
def add(x, y):
    result = x + y
    logger.info(f"{x} + {y} = {result}")
    return result
