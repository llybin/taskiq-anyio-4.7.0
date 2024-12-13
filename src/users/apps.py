import asyncio
import sys

import nest_asyncio
from asgiref.local import Local
from django.apps import AppConfig

from taskiq_app import broker

django_app_startup = Local()


class UsersConfig(AppConfig):
    name = "users"

    def ready(self):
        django_app_startup.running = True

        async def start_taskiq_broker():
            await broker.startup()

        nest_asyncio.apply()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(start_taskiq_broker())
