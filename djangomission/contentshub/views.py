from django.shortcuts import render

# Create your views here.


# 마스터 강의 개설
from contentshub.crud import master_klass_creator
from contentshub.models import Klass
from contentshub.ser import KlassSerializer
from utils.mixin import ListMixin, CreateMixin


class MasterKlassListCreateAPI(ListMixin, CreateMixin):
    queryset = Klass.objects.all()
    creator = staticmethod(master_klass_creator)
    serializer_class = KlassSerializer
