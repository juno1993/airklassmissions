from django.shortcuts import render

# Create your views here.
from contentshub.crud import master_klass_creator
from contentshub.models import Klass
from contentshub.ser import KlassSerializer
from utils.api_view import MasterAPIView
from utils.mixin import ListMixin, CreateMixin


# 마스터 강의 목록, 개설
class MasterKlassListCreateAPI(MasterAPIView, ListMixin, CreateMixin):
    queryset = Klass.objects.all()
    creator = staticmethod(master_klass_creator)
    serializer_class = KlassSerializer
    lookup_map = {
        'master_id': 'master_id'
    }

