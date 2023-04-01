import os
from celery import Celery
from datetime import timedelta

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# celery_app = Celery("config")
# celery_app.autodiscover_tasks()

# celery_app.conf.update(
#     broker_url='redis://localhost:6379',
#     result_backend='redis://localhost:6379',
#     accept_content="json",
#     task_serializer="json",
#     result_serializer="json",
#     result_expires=timedelta(days=1),
# )
