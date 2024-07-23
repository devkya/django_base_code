from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
import re

User = get_user_model()


def get_jwt(token: RefreshToken):
    """_summary_
    response 형식을 맞춰주기 위한 함수
    Args:
        user (User): 사용자

    Returns:
        dict: jwt 토큰
    """
    return {
        "jwt": {
            "access": str(token.access_token),
            "refresh": str(token),
        }
    }
