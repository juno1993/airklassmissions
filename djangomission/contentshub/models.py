from django.db import models


class Master(models.Model):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE, null=True, related_name='contentshub_master')
    name = models.CharField(max_length=10)


class Klass(models.Model):
    master = models.ForeignKey('contentshub.Master', on_delete=models.CASCADE, null=True, related_name='contentshub_klass')
    title = models.CharField(max_length=50)
