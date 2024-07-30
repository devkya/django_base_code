from .base import *
import environ

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, "env", "production.env"))

# GENERAL
DEBUG = False
ALLOWED_HOSTS = ["localhost", ] # TODO: 도메인, EC2  IP 추가해야 함

REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [
    "rest_framework.renderers.JSONRenderer",
]

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

# S3
# STATICFILES_STORAGE = "config.storages.StaticStorage"
# DEFAULT_FILE_STORAGE = "config.storages.MediaStorage"

# AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME")
# AWS_REGION = env.str("AWS_REGION")

# AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com"

# STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
# MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"
