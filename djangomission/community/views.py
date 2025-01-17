from django.shortcuts import render

# Create your views here.
from community.crud import user_question_creator, user_question_deleter, master_klass_answer_creator, \
    master_question_deleter
from community.models import Question
from community.ser import QuestionSerializer
from utils.api_view import UserAPIView, MasterAPIView
from utils.mixin import CreateMixin, DeleteMixin, ListMixin
from utils.permission import IsQuestionMine, IsMasterQuestionMine


# 유저 강의 질문 조회, 생성
class UserQuestionListCreateAPI(UserAPIView, ListMixin, CreateMixin):
    queryset = Question.objects.all()
    creator = staticmethod(user_question_creator)
    serializer_class = QuestionSerializer
    lookup_map = {
        'klass_id': 'klass_id'
    }


# 유저 강의 질문 삭제
class UserQuestionDeleteAPI(UserAPIView, DeleteMixin):
    model = Question
    permission_classes = (
        IsQuestionMine,
    )
    deleter = staticmethod(user_question_deleter)
    lookup_map = {
        'question_id': 'id',
        'klass_id': 'klass_id'
    }


# 마스터 질문 삭제
class MasterQuestionDeleteAPI(MasterAPIView, DeleteMixin):
    model = Question
    permission_classes = (
        IsMasterQuestionMine,
    )
    deleter = staticmethod(master_question_deleter)
    lookup_map = {
        'question_id': 'id',
        'klass_id': 'klass_id'
    }


# 마스터 강의 답변 생성
class MasterKlassAnswerCreateAPI(MasterAPIView, CreateMixin):
    permission_classes = (
        IsMasterQuestionMine,
    )
    creator = staticmethod(master_klass_answer_creator)
