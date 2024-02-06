from rest_framework.exceptions import APIException
from rest_framework.response import Response


# TODO: 에러 코드 정리 필요
class CustomException(APIException):
    name = "CustomException"

    def __init__(self, detail=""):
        self.detail = detail

    def __str__(self):
        return f"{self.name}({self.code}): {self.message}"

    def add_detail(self, detail):
        self.detail = detail

    def response(self):
        return Response(
            {
                "success": False,
                "message": self.message,
                "detail": self.detail,
                "code": self.code,
            }
        )


####################################
# old csound server error
class CSoundSignInFailed(CustomException):
    name = "CSoundSignInFailed"
    message = "이전 서버에서 로그인에 실패하였습니다.(관리자에게 문의하세요)"
    code = "C001"


class CSoundDeviceNotFound(CustomException):
    name = "CSoundDeviceNotFound"
    message = "이전 서버에 존재하지 않는 디바이스 또는 VUZIX, VUZIX2 모델이 아닙니다."
    code = "C002"


class CSoundUserNotFound(CustomException):
    name = "CSoundUserNotFound"
    message = "디바이스에 할당된 유저가 존재하지 않습니다.(관리자에게 문의하세요)"
    code = "C003"


class CSoundDeviceIsNotNormal(CustomException):
    name = "CSoundDeviceIsNotNormal"
    message = "디바이스가 [정상]타입이 아닙니다.(관리자에게 문의하세요)"
    code = "C004"


####################################
# Auth 에러
class AuthFailed(CustomException):
    name = "AuthFailed"
    message = "사용자 인증에 실패하였습니다."
    code = "A001"


class DeviceAlreadyRegistered(CustomException):
    name = "DeviceAlreadyRegistered"
    message = "이미 마이그레이션 진행한 디바이스입니다(관리자에게 문의하세요)."
    code = "A002"


class NotTermsAgreed(CustomException):
    name = "NotTermsAgreed"
    message = "약관에 동의하지 않았습니다."
    code = "A003"


####################################
# 존재하지 않음
class UserNotFound(CustomException):
    name = "UserNotFound"
    message = "유저가 존재하지 않습니다(관리자에게 문의하세요)."
    code = "F001"


class LicenseNotFound(CustomException):
    name = "LicenseNotFound"
    message = "라이센스가 존재하지 않습니다."
    code = "F002"


class DeviceNotFound(CustomException):
    name = "DeviceNotFound"
    message = "디바이스가 존재하지 않습니다."
    code = "F003"


class ApkNotFound(CustomException):
    name = "ApkNotFound"
    message = "APK가 존재하지 않습니다."
    code = "F004"


####################################
# 요청 에러
class MissingRequest(CustomException):
    name = "InvalidRequest"
    message = "잘못된 요청입니다."
    code = "R001"


class InvalidRequest(CustomException):
    name = "InvalidRequest"
    message = "유효하지 않은 요청입니다."
    code = "R002"


####################################
# Token 에러
class InvalidToken(CustomException):
    name = "InvalidToken"
    message = "잘못된 토큰입니다."
    code = "T001"


class MissingHeader(CustomException):
    name = "MissingHeader"
    message = "헤더가 존재하지 않습니다."
    code = "T002"


####################################
# 서버 에러
class ServerError(CustomException):
    name = "ServerError"
    message = "서버 에러입니다."
    code = "S001"


# DB 에러
class DBError(CustomException):
    name = "DBError"
    message = "DB 에러입니다."
    code = "S002"
