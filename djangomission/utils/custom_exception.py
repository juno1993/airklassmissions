"""
직접 정의한 Exception 들을 저장하는 모듈입니다.
"""

from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import exception_handler


class ForbiddenException(APIException):
    def __init__(self, message):
        self.message = message


class BadRequestException(APIException):
    def __init__(self, message):
        self.message = message


class NotFoundException(APIException):
    def __init__(self, model, **filters):
        self.model = model
        self.filters = filters

    @property
    def message(self):
        filter_message = ', '.join([f'{key}={value}' for key, value in self.filters.items()])
        return '{}에서 {} 조건에 해당하는 항목을 찾을 수 없습니다.'.format(self.model.__name__, filter_message)


class InternalServerException(APIException):
    def __init__(self, message):
        self.message = message


def custom_exception_handler(exc, context):
    """
    API View 내에서 발생한 모든 Exception 은 해당 함수가 처리하게 됩니다.
    """
    if isinstance(exc, BadRequestException):
        return Response({'message': exc.message}, status=400)
    elif isinstance(exc, ForbiddenException):
        return Response({'message': exc.message}, status=403)
    elif isinstance(exc, NotFoundException):
        return Response({'message': exc.message}, status=404)
    elif isinstance(exc, InternalServerException):
        return Response({'message': exc.message}, status=500)

    else:
        return exception_handler(exc, context)
