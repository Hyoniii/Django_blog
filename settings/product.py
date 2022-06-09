from .base import *
from my_settings import DATABASES, SECRETKEY

SECRET_KEY = SECRETKEY

DEBUG = False

ALLOWED_HOSTS = []  # 추후에 배포하면 추가

DATABASES = DATABASES
