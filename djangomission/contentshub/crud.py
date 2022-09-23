



from contentshub.models import Klass


# 클래스 생성
def master_klass_creator(request, **kwargs):
    data = request.data
    data['master'] = request.user.contentshub_master
    Klass.objects.create(**data)


