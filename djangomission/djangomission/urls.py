"""djangomission URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from accounts.views import *
from community.views import *
from contentshub.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('klass', KlassListAPI.as_view()),      # 전체 강의 목록

    # 강사
    path('master/<int:master_id>/', include([
        path('klass', MasterKlassListCreateAPI.as_view()),
        path('klass/<int:klass_id>/question/<int:question_id>', MasterQuestionDeleteAPI.as_view()),
        path('question/<int:question_id>/answer', MasterKlassAnswerCreateAPI.as_view())
    ])),

    # 유저
    path('user/login', UserLoginAPI.as_view()),
    path('user/<int:user_id>/', include([
        path('klass/<int:klass_id>/question', UserQuestionListCreateAPI.as_view()),
        path('klass/<int:klass_id>/question/<int:question_id>', UserQuestionDeleteAPI.as_view())
    ]))
]
