from channels.middleware import BaseMiddleware
from channels.db import database_sync_to_async

from django.db import close_old_connections
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework_simplejwt.exceptions import TokenError
from config.exceptions import InvalidToken, MissingHeader

import json


class TokenAuthMiddleware(BaseMiddleware):
    # 연결이 이루어질 때마다 호출됨
    async def __call__(self, scope, receive, send):
        close_old_connections()
        headers = dict(scope["headers"])

        if b"authorization" in headers:
            # 토큰을 추출하고 검증
            token_name, token_key = headers[b"authorization"].decode().split()
            if token_name == "Bearer":
                user = await self.get_user_from_token(token_key)
                if user:
                    scope["user"] = user
                    return await super().__call__(scope, receive, send)
                else:
                    await self.accept(send)
                    await self.send_invalid_token(send)

        # 유효한 토큰이 없으면 연결을 거부합니다.
        else:
            await self.accept(send)
            await self.send_missing_header(send)

    @database_sync_to_async
    def get_user_from_token(self, token):
        # 유저 반환
        try:
            valid_data = JWTAuthentication().get_validated_token(token)
            user = JWTAuthentication().get_user(valid_data)
            return user

        except Exception as e:
            return None

    async def accept(self, send):
        # 연결 수락
        await send({"type": "websocket.accept"})

    async def send_invalid_token(self, send):
        error = InvalidToken()
        error_data = {
            "success": False,
            "message": error.message,
            "detail": error.detail,
            "code": error.code,
        }
        error_json = json.dumps(error_data)
        await send({"type": "websocket.close", "reason": error_json})

    async def send_missing_header(self, send):
        error = MissingHeader()
        error_data = {
            "success": False,
            "message": error.message,
            "detail": error.detail,
            "code": error.code,
        }
        error_json = json.dumps(error_data)
        await send({"type": "websocket.close", "reason": error_json})
