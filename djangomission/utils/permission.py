from django.apps import apps
from rest_framework import permissions

from utils.query_helper import get_object_or_404


# 유저 본인 질문인지 체크
class IsQuestionMine(permissions.BasePermission):
    def has_permission(self, request, view):
        question = get_object_or_404(apps.get_model('community.Question'), id=view.kwargs.get('question_id'))
        if request.user != question.user:
            return None
        else:
            return True


# 마스터 본인 클래스인지 확인
class IsMasterKlassMine(permissions.BasePermission):
    def has_permission(self, request, view):
        question = get_object_or_404(apps.get_model('community.Question'), id=view.kwargs.get('question_id'))
        if request.user != question.klass.master.user:
            return None
        else:
            return True
