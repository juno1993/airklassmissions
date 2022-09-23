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

from accounts.views import UserLoginAPI
from community.views import UserQuestionListCreateAPI, UserQuestionDeleteAPI, MasterKlassAnswerCreateAPI
from contentshub.views import MasterKlassListCreateAPI

urlpatterns = [
    path('admin/', admin.site.urls),

    path('master/', include([
        path('klass', MasterKlassListCreateAPI.as_view()),
        path('question/<int:question_id>/answer', MasterKlassAnswerCreateAPI.as_view())
    ])),

    path('user/', include([
        path('login', UserLoginAPI.as_view()),
        path('klass/<int:klass_id>/question', UserQuestionListCreateAPI.as_view()),
        path('klass/<int:klass_id>/question/<question_id>', UserQuestionDeleteAPI.as_view())
    ]))
]
