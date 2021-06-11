from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

celery_app2 = Celery('tasks', broker='pyamqp://guest@rabbit//', include=['worker', 'worker2'])
