from django.core.management.base import BaseCommand

from accounts.models import User
from contentshub.models import Master


class Command(BaseCommand):
    def handle(self, *args, **options):
        # 유저 생성
        user_data = {
            'username': 'person1',
            'name': '사람1',
            'password': 'lp1234'
        }
        user = User.objects.create(**user_data)
        user.set_password(user_data['password'])
        user.save()
        self.stdout.write(self.style.SUCCESS(f'Successfully created user {user.username}'))

        # 마스터 생성
        Master.objects.create(user=user, name='master1')
