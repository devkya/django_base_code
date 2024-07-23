from .base import *
import environ
from config.celery_schedule import CELERY_BEAT_SCHEDULE

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, "env", "development.env"))

# GENERAL
DEBUG = True
ALLOWED_HOSTS = ["*"]

# DB
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("DB_NAME"),
        "USER": env.str("DB_USER"),
        "PASSWORD": env.str("DB_PASSWORD"),
        "HOST": env.str("DB_HOST"),
        "PORT": env.str("DB_PORT"),
    }
}

# CHANNEL
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("dev-app-redis", 6379)],
        },
    },
}

# CELERY
CELERY_BROKER_URL = "redis://dev-app-redis:6379/0"
CELERY_RESULT_BACKEND = "redis://dev-app-redis:6379/0"
CELERY_BEAT_SCHEDULE = CELERY_BEAT_SCHEDULE
