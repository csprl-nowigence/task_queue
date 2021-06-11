from celery import Celery

app = Celery('task', broker='pyamqp://guest@rabbit//')

