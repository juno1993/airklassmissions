from community.models import Question, Answer
from utils.custom_exception import ForbiddenException
from utils.query_helper import get_object_or_None


# 유저 강의 질문 생성
def user_question_creator(request, **kwargs):
    data = request.data
    data['user'] = request.user
    data['klass_id'] = kwargs.get('klass_id')
    Question.objects.create(**data)


# 유저 강의 질문 삭제
def user_question_deleter(obj):
    # 답변 달린 질문 삭제 불가능
    if obj.community_answer.exists():
        raise ForbiddenException('답변달린 질문은 삭제가 불가능합니다.')
    else:
        obj.delete()


# 강사 질문 삭제
def master_question_deleter(obj):
    if not obj.community_answer.exists():
        obj.delete()
    else:
        raise ForbiddenException('답변이 달린 질문은 삭제가 불가능 합니다.')


# 마스터 강의 답변 생성
def master_klass_answer_creator(request, **kwargs):
    data = request.data
    data['master'] = request.user.contentshub_master
    data['question_id'] = kwargs.get('question_id')

    answer = get_object_or_None(Answer, master=data['master'], question_id=data['question_id'])
    if not answer:
        Answer.objects.create(**data)
    else:
        raise ForbiddenException('이미 질문에 답변이 존재합니다.')
