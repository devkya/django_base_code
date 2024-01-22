# 참고용으로 사용할 수 있는 openapi 예시
# from drf_spectacular.utils import inline_serializer
# from drf_spectacular.utils import extend_schema_serializer
# from rest_framework import serializers
# from rest_framework import serializers
# from users.serializers import (
#     UserSerializer,
#     UserLicenseSerializer,
#     UserDeviceSerializer,
#     TermsSerializer,
# )
# from supports.serializers import ApkSerializer
# from drf_spectacular.utils import OpenApiParameter, OpenApiExample
# from drf_spectacular.types import OpenApiTypes


# def generate_errors_response(errors):
#     result = {}
#     for err in errors:
#         data = inline_serializer(
#             name=err.name,
#             fields={
#                 "success": serializers.BooleanField(default=False),
#                 "code": serializers.CharField(default=err.code),
#                 "message": serializers.CharField(default=err.message),
#                 "detail": serializers.CharField(default=""),
#             },
#         )
#         result.update({err.code: data})
#     return result


# class JWTSerializer(serializers.Serializer):
#     access = serializers.CharField()
#     refresh = serializers.CharField()


# class DeviceRegisterReqSerializer(serializers.Serializer):
#     uid = serializers.CharField(help_text="사용자 uid")
#     sn = serializers.CharField(help_text="디바이스 시리얼 넘버")
#     dt = serializers.CharField(help_text="디바이스 타입")


# class AuthResSerializer(serializers.Serializer):
#     success = serializers.BooleanField(default=True)
#     user = UserSerializer(many=False)
#     license = UserLicenseSerializer(many=False)
#     device = UserDeviceSerializer(many=False)
#     jwt = JWTSerializer(many=False)


# class TermsResSerializer(serializers.Serializer):
#     success = serializers.BooleanField(default=True)
#     terms = TermsSerializer(many=False)


# class ApkResSerializer(serializers.Serializer):
#     success = serializers.BooleanField(default=True)
#     apk = ApkSerializer(many=False)


# authorization_parameter = [
#     OpenApiParameter(
#         name="Authorization",
#         type=OpenApiTypes.STR,
#         description="Bearer [access token]",
#         required=True,
#         location=OpenApiParameter.HEADER,
#         examples=[
#             OpenApiExample(
#                 name="Bearer [access token]",
#                 value="입력하지 않아도 됩니다.",
#             ),
#         ],
#     )
# ]
