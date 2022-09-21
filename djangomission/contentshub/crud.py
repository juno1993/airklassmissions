



from contentshub.models import Klass


# 클래스 생성
def master_klass_creator(request, **kwargs):
    data = request.data
    Klass.objects.create(**data)
    return True
