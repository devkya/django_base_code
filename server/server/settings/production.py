from .base import *
import environ
from config.celery_schedule import CELERY_BEAT_SCHEDULE

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, "env", "production.env"))

# GENERAL
DEBUG = False
ALLOWED_HOSTS = []

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
            "hosts": [("prod-redis", 6379)],
        },
    },
}

# CELERY
CELERY_BROKER_URL = "redis://prod-redis:6379/0"
CELERY_RESULT_BACKEND = "redis://prod-redis:6379/0"
CELERY_BEAT_SCHEDULE = CELERY_BEAT_SCHEDULE

# S3
# STATICFILES_STORAGE = "config.storages.StaticStorage"
# DEFAULT_FILE_STORAGE = "config.storages.MediaStorage"

# AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME")
# AWS_REGION = env.str("AWS_REGION")

# AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com"

# STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
# MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"
