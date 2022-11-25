# app/tasks.py, 可以复用的task
from celery import shared_task
from django_tutorial.celery import app
import time
from .views import musiclist_crawler

# @shared_task
# @app.task(queue='test')
# @app.task()
# def add_asfsf(x, y):
#     time.sleep(2)
#     return x + y

@shared_task
def add_musiclist(x, y):
    # time.sleep(2)
    musiclist_crawler()
    myword = 'its success!!!!!!!!'
    return myword