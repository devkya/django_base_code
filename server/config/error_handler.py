from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework_simplejwt.exceptions import TokenError
from psycopg2 import Error as DBError
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.views import exception_handler
from rest_framework.response import Response
from users.models import CustomUser, UserLicense, UserDevice
from supports.models import Apk
from .exceptions import *
import traceback
import logging


logger = logging.getLogger("CSOUND")


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    ############################################
    # Old CSound 서버 에러
    if isinstance(exc, CSoundSignInFailed):
        error = CSoundSignInFailed()
        return error.response()

    # Old CSound 계정 없음
    if isinstance(exc, CSoundUserNotFound):
        error = CSoundUserNotFound()
        logger.critical(
            f"{error.message}",
            extra={"view_name": context["view"].__class__.__name__},
        )
        return error.response()

    if isinstance(exc, CSoundDeviceNotFound):
        error = CSoundDeviceNotFound()
        return error.response()

    if isinstance(exc, CSoundDeviceIsNotNormal):
        error = CSoundDeviceIsNotNormal()
        return error.response()

    ############################################
    # 로그인 실패
    if isinstance(exc, AuthenticationFailed):
        error = AuthFailed()
        return error.response()

    # 토큰 만료 & 잘못된 토큰
    if isinstance(exc, TokenError):
        error = InvalidToken()
        return error.response()

    if isinstance(exc, UserDevice.DoesNotExist):
        error = DeviceNotFound()
        return error.response()

    # 라이센스 존재하지 않음
    if isinstance(exc, UserLicense.DoesNotExist):
        error = LicenseNotFound()
        return error.response()

    # 유저가 존재하지 않음
    if isinstance(exc, CustomUser.DoesNotExist):
        error = UserNotFound()
        return error.response()

    # APK가 존재하지 않음
    if isinstance(exc, Apk.DoesNotExist):
        error = ApkNotFound()
        return error.response()

    # migration 에러
    if isinstance(exc, DeviceAlreadyRegistered):
        error = DeviceAlreadyRegistered()
        return error.response()

    ############################################
    # 잘못된 요청(DRF) - 요청이 오지 않음
    if isinstance(exc, ValidationError):
        error = MissingRequest()
        error.add_detail(detail=exc.detail)

        return error.response()

    # 잘못된 요청(Django) - 유효하지 않음
    if isinstance(exc, DjangoValidationError):
        error = InvalidRequest()
        error.add_detail(detail=exc.messages)
        return error.response()

    ############################################
    # DB 에러
    if isinstance(exc, DBError):
        error = DBError()
        error.add_detail(detail=exc.detail)
        return error.response()

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
