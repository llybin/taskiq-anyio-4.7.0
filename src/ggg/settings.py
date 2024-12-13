import os
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "off") == "on"

# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = []

LOCAL_APPS = [
    "users",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


RMQ_USER = os.environ.get("RMQ_USER")
RMQ_PASSWORD = os.environ.get("RMQ_PASSWORD")
RMQ_HOST = os.environ.get("RMQ_HOST")
RMQ_PORT = os.environ.get("RMQ_PORT")
RMQ_NAME = os.environ.get("RMQ_NAME")
TASKIQ_BROKER_URL = f"amqp://{RMQ_USER}:{RMQ_PASSWORD}@{RMQ_HOST}:{RMQ_PORT}/{RMQ_NAME}"
