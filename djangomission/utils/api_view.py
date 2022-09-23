from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.authentication import MasterAuthentication, UserAuthentication
from utils.query_helper import get_object_or_404


class CustomAPIView(APIView):
    queryset = None
    creator = None
    deleter = None
    serializer_class = None

    model = None
    lookup_map = {}

    authentication_classes = ()

    @staticmethod
    def success(detail='success', **kwargs):
        return Response({'detail': detail, **kwargs})

    @staticmethod
    def response(data, status_code=200):
        return Response(data, status=status_code)

    def get_object(self, request, **kwargs):
        query_dict = {val: kwargs.get(key) for key, val in self.lookup_map.items()}
        obj = get_object_or_404(self.model, **query_dict)
        return obj

    def list(self, request, **kwargs):
        queryset = self.queryset
        # 필터
        queryset = queryset.filter(**{val: kwargs.get(key) for key, val in self.lookup_map.items()})
        ser = self.serializer_class(instance=queryset, many=True)
        return self.response(ser.data)

    def create(self, request, **kwargs):
        result = self.creator(request, **kwargs)
        return self.response(result) if result else self.success()

    def delete(self, request, **kwargs):
        obj = self.get_object(request, **kwargs)
        result = self.deleter(obj)
        return self.response(result) if result else self.success()


# 마스터 권한 체크
class MasterAPIView(CustomAPIView):
    def __init__(self, *args, **kwargs):
        self.authentication_classes += (
            MasterAuthentication,
        )
        self.permission_classes += (
            permissions.IsAuthenticated,
        )
        super().__init__(*args, **kwargs)


# 유저 권한 체크
class UserAPIView(CustomAPIView):
    def __init__(self, *args, **kwargs):
        self.authentication_classes += (
            UserAuthentication,
        )
        self.permission_classes += (
            permissions.IsAuthenticated,
        )
        super().__init__(*args, **kwargs)
