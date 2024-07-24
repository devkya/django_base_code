from pathlib import Path
import environ
from datetime import timedelta
import os


BASE_DIR = Path(__file__).resolve().parents[2]

# 필요한 디렉토리 생성
os.makedirs(os.path.join(BASE_DIR, "logs"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "static"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "media"), exist_ok=True)

# env 파일 읽기
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, "env", "base.env"))

LOGGING_NAME = env.str("LOGGING_NAME")
SECRET_KEY = env.str("SECRET_KEY")

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third party
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "corsheaders",
    "drf_spectacular",
    "django_cleanup.apps.CleanupConfig",
    # Apps
    "stream",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        # "rest_framework.permissions.IsAuthenticated",
        "rest_framework.permissions.AllowAny",  # TODO: simplejwt 구현 후 변경
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",  # drf-spectacular
    "EXCEPTION_HANDLER": "config.exception_handler.custom_exception_handler",
}

SIMPLE_JWT = {
    # "SIGNING_KEY": env.str("SIGNING_KEY"), # 기본값은 SECRET_KEY
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),  # TODO: 정해야 함
    "REFRESH_TOKEN_LIFETIME": timedelta(days=90),  # TODO: 정해야 함
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,
    "ALGORITHM": "HS256",
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    # "USER_ID_FIELD": "uid", # TODO: user 모델의 pk 필드명
    # "USER_ID_CLAIM": "user_uid" # TODO: claim에 추가할 변수명
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Your Project API",
    "DESCRIPTION": "Your project description",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    # OTHER SETTINGS
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[{server_time}] {message}",
            "style": "{",
        },
        "standard": {"format": "%(asctime)s [%(levelname)s][%(name)s]: %(message)s"},
    },
    "handlers": {
        "console": {
            "level": "INFO",
            # "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
        },
        "django.server": {
            "level": "WARNING",
            "class": "logging.StreamHandler",
            # "filters": ["require_debug_false"],
            "formatter": "django.server",
        },
        "file": {
            "level": "ERROR",
            "encoding": "utf-8",
            "filters": ["require_debug_false"],
            "class": "logging.handlers.RotatingFileHandler",
            "filename": BASE_DIR / "logs/error.log",
            "maxBytes": 1024 * 1024 * 10,  # 5 MB
            "backupCount": 10,
            "formatter": "standard",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
        },
        "django.server": {
            "handlers": ["django.server"],
            "level": "INFO",
            "propagate": True,
        },
        LOGGING_NAME: {
            "handlers": ["console", "file"],
            "level": "ERROR",
        },  # TODO: 로깅 이름 변경(base.env)
    },
}


# CORS
CORS_ALLOW_ALL_ORIGINS = True  # TODO: False로 변경
# CORS_ALLOWED_ORIGINS = []  # TODO: http://localhost:[port] 추가, 도메인 추가
CSRF_TRUSTED_ORIGINS = []  # TODO: http://localhost:[port] 추가, 도메인 추가

ROOT_URLCONF = "server.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "server.wsgi.application"


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Language & Timezone
LANGUAGE_CODE = "ko-kr"
TIME_ZONE = "Asia/Seoul"
USE_I18N = True
USE_TZ = True


# STATIC & MEDIA
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(
    BASE_DIR, "staticfiles"
)  # collectstatic 수행 시 정적 파일을 모으는 장소
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "app", "static"),  # TODO: app 내에 static 폴더 생성 후 정적 파일 관리
# ]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
