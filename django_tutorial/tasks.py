# myproject/tasks.py
# 专属于myproject项目的任务
from celery import Celery

app = Celery('django_tutorial')
@ app.task
def test():
    pass