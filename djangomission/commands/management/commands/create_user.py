from getpass import getpass

from django.core.management.base import BaseCommand, CommandError

from accounts.models import User
from contentshub.models import Master


class Command(BaseCommand):
    help = '유저 생성'

    def handle(self, *args, **options):
        username = input('Username: ')
        password = getpass('Password: ')
        name = input('Name: ')

        user = User.objects.create(username=username, name=name)
        user.set_password(password)
        user.save()
        Master.objects.create(user=user, name=name)
        self.stdout.write(self.style.SUCCESS(f'Successfully created user {user.username}'))

        # if User.objects.exists():
        #     raise CommandError('이미 회원이 생성되었습니다.')
        # for i in range(1, 3):
        #     user_data = {
        #         'username': f"person{i}",
        #         'name': f"사람{i}",
        #         'password': 'lp1234'
        #     }
        #     user = User.objects.create(**user_data)
        #     user.set_password(user_data['password'])
        #     user.save()
        #
        #     # 마스터 생성
        #     Master.objects.create(user=user, name=f"master{i}")
        #     self.stdout.write(self.style.SUCCESS(f'Successfully created user {user.username}'))
