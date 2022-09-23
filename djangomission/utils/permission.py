from django.apps import apps
from rest_framework import permissions

from utils.query_helper import get_object_or_404


# 유저 본인 질문인지 체크
class IsQuestionMine(permissions.BasePermission):
    message = '요청하신 User의 질문이 아닙니다.'

    def has_permission(self, request, view):
        question = get_object_or_404(apps.get_model('community.Question'), id=view.kwargs.get('question_id'))
        if request.user != question.user:
            return None
        else:
            return True


# 마스터 본인 클래스 질문인지 체크
class IsMasterQuestionMine(permissions.BasePermission):
    message = '요청하신 Master의 Klass가 아닙니다.'
    
    def has_permission(self, request, view):
        question = get_object_or_404(apps.get_model('community.Question'), id=view.kwargs.get('question_id'))
        if request.user != question.klass.master.user:
            return None
        else:
            return True


# 마스터 본인인지 확인
class IsMatchedMasterId(permissions.BasePermission):
    """
    요청한 master_id와 url param 의 master_id가 일치하는지 확인
    """
    message = '요청하신 master id와 토큰값이 알맞지 않습니다.'

    def has_permission(self, request, view):
        return request.user.contentshub_master.id == int(view.kwargs.get('master_id'))


# 유저 본인인지 확인
class IsMatchedUserId(permissions.BasePermission):
    """
    요청한 user_id와 url param 의 user_id가 일치하는지 확인
    """

    message = '요청하신 user id와 토큰값이 알맞지 않습니다.'

    def has_permission(self, request, view):
        return request.user.id == int(view.kwargs.get('user_id'))
