import os
import sys
from pathlib import Path

import django
from django.conf import settings
from taskiq import TaskiqMiddleware, TaskiqScheduler
from taskiq.schedule_sources import LabelScheduleSource
from taskiq_aio_pika import AioPikaBroker


class DjangoMiddleware(TaskiqMiddleware):
    def startup(self):
        sys.path.append(str(Path.cwd()))
        from users.apps import django_app_startup

        if not getattr(django_app_startup, "running", False):
            os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ggg.settings")
            django.setup(set_prefix=False)


broker = AioPikaBroker(url=settings.TASKIQ_BROKER_URL)

broker = broker.with_middlewares(DjangoMiddleware())

scheduler = TaskiqScheduler(broker=broker, sources=[LabelScheduleSource(broker)])
