from rest_framework.views import exception_handler
from .exceptions import *
from django.conf import settings
import traceback
import logging


logger = logging.getLogger(settings.LOGGING_NAME)


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    # 서버 에러
    if response is None or isinstance(exc, ServerError):
        detail = "\n" + traceback.format_exc()
        # detail = exc.detail
        error = ServerError()
        error.add_detail(detail=detail)
        logger.critical(
            f"{detail}",
            extra={"view_name": context["view"].__class__.__name__},
        )
        return error.response()

    return response
