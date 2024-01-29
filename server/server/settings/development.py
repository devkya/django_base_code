from .base import *
import environ

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, "env", "development.env"))

DEBUG = True
ALLOWED_HOSTS = ["*"]

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

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("dev-redis", 6379)],
        },
    },
}

# CELERY
CELERY_BROKER_URL = "redis://dev-redis:6379/0"
CELERY_RESULT_BACKEND = "redis://dev-redis:6379/0"
# CELERY_BEAT_SCHEDULE = {
#     "테스트": {
#         "task": "analysis.tasks.test_celery",
#         "schedule": timedelta(seconds=10),
#     }
# }
