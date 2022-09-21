from rest_framework.response import Response
from rest_framework.views import APIView

from utils.query_helper import get_object_or_None


class CustomAPIView(APIView):
    queryset = None
    creator = None
    deleter = None
    serializer_class = None

    model = None
    lookup_map = {}

    @staticmethod
    def success(detail='success', **kwargs):
        return Response({'detail': detail, **kwargs})

    @staticmethod
    def response(data, status_code=200):
        return Response(data, status=status_code)

    def get_object(self, request, **kwargs):
        query_dict = {val: kwargs.get(key) for key, val in self.lookup_map.items()}
        obj = get_object_or_None(self.model, **query_dict)
        return obj

    def list(self, request, **kwargs):
        queryset = self.queryset
        # 필터
        queryset = queryset.filter(**{val: kwargs.get(key) for key, val in self.lookup_map.items()})
        ser = self.serializer_class(instance=queryset, many=True)
        return self.response(ser.data)

    def creator(self, request, **kwargs):
        result = self.creator(request, **kwargs)
        return self.response(result) if result else self.success()

    def deleter(self, request, **kwargs):
        obj = self.get_object(request, **kwargs)
        result = self.deleter(obj)
        return self.response(result) if result else self.success()
