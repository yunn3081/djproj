import os
from celery import Celery
from datetime import timedelta
from celery.schedules import crontab
import pytz
from django.conf import settings

# 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_tutorial.settings')

# 实例化
app = Celery('django_tutorial')
# app.conf.enable_utc=f=False
# app.conf.timezone='Asia/Taipei'
# local_timezone = pytz.timezone('Asia/Taipei')
# namespace='CELERY'作用是允许你在Django配置文件中对Celery进行配置
# 但所有Celery配置项必须以CELERY开头，防止冲突
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.config_from_object('django_tutorial.celeryconfig')

# 自动从Django的已注册app中发现任务
app.autodiscover_tasks()


# 一个测试任务
# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')

# 固定的定時任務
app.conf.beat_schedule = {
    # 'add-every-monday-morning': {
    #     'task': 'musics.tasks.add_musiclist',
    #     'schedule': crontab(minute='*/1'),
    #     # 'schedule': crontab(minute='*/1'),
    #     'args': (8, 16),
    # },
    'my_musiclist': {
        'task': 'musics.tasks.add_musiclist',
        'schedule': crontab(hour=0, minute=0),#, day_of_week='*'),
        # 'schedule': crontab(minute='*/1'),
        'args': (13, 8),
    },


}

#print(app.conf.__dict__)