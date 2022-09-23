from django.db import models


class Question(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, null=True, related_name='community_question')
    klass = models.ForeignKey('contentshub.Klass', on_delete=models.CASCADE, null=True, related_name='community_question')
    contents = models.TextField()

    class Meta:
        ordering = ('-id',)


class Answer(models.Model):
    master = models.ForeignKey('contentshub.Master', on_delete=models.CASCADE, null=True, related_name='community_answer')
    question = models.ForeignKey('community.Question', on_delete=models.CASCADE, null=True, related_name='community_answer')
    contents = models.TextField()

    class Meta:
        ordering = ('-id',)
